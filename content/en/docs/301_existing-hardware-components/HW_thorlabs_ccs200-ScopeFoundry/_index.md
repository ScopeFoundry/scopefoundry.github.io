
---
title: HW_thorlabs_ccs200 (ScopeFoundry)
description: No description available.
weight: 49
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_thorlabs_ccs200)
- Last Updated: 2025-11-03T22:37:41Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_thorlabs_ccs200 ScopeFoundryHW/thorlabs_ccs200
```


## Readme
# Thorlabs CCS200 Spectrometer Hardware Component

ScopeFoundry hardware component for the Thorlabs CCS200 compact CCD spectrometer.

## Overview

This hardware component provides integration of the Thorlabs CCS200 spectrometer into the ScopeFoundry framework. The CCS200 is a compact, fiber-coupled spectrometer with 3648 pixels covering a wavelength range from approximately 200-1000 nm.

## Files

- `thorlabs_ccs200_interface.py` - Low-level interface to the TLCCS DLL
- `thorlabs_ccs200_hw.py` - ScopeFoundry HardwareComponent wrapper
- `ccs200_spec_live.py` - Live spectrum measurement with plotting
- `ccs200_spec_live.ui` - Qt UI file for the live measurement
- `ccs200_test_app.py` - Example ScopeFoundry application
- `ccs200_simple_test.py` - Standalone test script (no ScopeFoundry required)
- `__init__.py` - Package initialization

## Requirements

### Hardware
- Thorlabs CCS200 spectrometer
- USB connection to computer

### Software
- Thorlabs CCS200 driver and TLCCS DLL
  - Default location: `C:\Program Files\IVI Foundation\VISA\Win64\Bin\TLCCS_64.dll`
  - Download from: https://www.thorlabs.com/software_pages/ViewSoftwarePage.cfm?Code=CCS
- Python packages:
  - ScopeFoundry
  - numpy
  - matplotlib (for testing)

## Installation

1. Install the Thorlabs CCS200 driver software
2. Copy this directory to your ScopeFoundryHW folder
3. The component should be importable as:
   ```python
   from ScopeFoundryHW.thorlabs_ccs200 import ThorlabsCCS200SpectrometerHW
   ```

## Usage

### In a ScopeFoundry Application

```python
from ScopeFoundry import BaseMicroscopeApp
from ScopeFoundryHW.thorlabs_ccs200 import ThorlabsCCS200SpectrometerHW, CCS200SpecLive

class MyApp(BaseMicroscopeApp):
    def setup(self):
        # Add the hardware component
        self.add_hardware(ThorlabsCCS200SpectrometerHW(self))

        # Add the live spectrum measurement
        self.add_measurement(CCS200SpecLive(self))

if __name__ == '__main__':
    import sys
    app = MyApp(sys.argv)
    sys.exit(app.exec_())
```

### Configuration

Before connecting, configure the following settings:

- **resource_name**: VISA resource string for your device
  - Example: `'USB0::0x1313::0x8089::M00853523::RAW'`
  - Find your device's resource name using NI-VISA or Thorlabs software
- **dll_path**: Path to the TLCCS_64.dll file
  - Default: `r"C:\Program Files\IVI Foundation\VISA\Win64\Bin"`
- **int_time**: Integration time in seconds (0.00001 to 60 s)
  - Default: 0.01 s (10 ms)

### Acquiring Spectra

```python
# In a measurement or other code with access to the hardware component:
hw = app.hardware['thorlabs_ccs200_spec']

# Acquire a spectrum
hw.acquire_spectrum()

# Get the spectrum data
spectrum = hw.get_spectrum()
wavelengths = hw.get_wavelengths()

# Plot or process the data
import matplotlib.pyplot as plt
plt.plot(wavelengths, spectrum)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.show()
```

### Standalone Usage (Without ScopeFoundry)

```python
from ScopeFoundryHW.thorlabs_ccs200 import ThorlabsCCS200Spectrometer

# Connect to spectrometer
spec = ThorlabsCCS200Spectrometer(
    resource_name='USB0::0x1313::0x8089::M00853523::RAW',
    debug=True
)

# Set integration time (in seconds)
spec.set_integration_time_sec(0.01)

# Acquire spectrum
spectrum = spec.acquire_spectrum()
wavelengths = spec.wavelengths

# Close when done
spec.close()
```

## Testing

### Simple Test (No ScopeFoundry)
```bash
cd ScopeFoundryHW/thorlabs_ccs200
python ccs200_simple_test.py
```

### ScopeFoundry Test Application
```bash
cd ScopeFoundryHW/thorlabs_ccs200
python ccs200_test_app.py
```

## Live Measurement Features

The `CCS200SpecLive` measurement provides:

- **Real-time spectrum plotting** with pyqtgraph
- **Continuous or single-shot acquisition**
- **Background subtraction** - capture and subtract background spectrum
- **Baseline subtraction** - subtract a constant offset value
- **ROI (Region of Interest)** - select wavelength range and calculate integrated intensity
- **Data saving** - save spectra to HDF5 files with full metadata
- **Auto-save** - automatically save data after single-shot acquisitions

### Using the Live Measurement

1. Run the test application: `python ccs200_test_app.py`
2. Check "HW Connect" to connect to the spectrometer
3. Adjust integration time as needed
4. Check "Run" to start acquisition
5. Use the ROI selector on the plot to define wavelength range of interest
6. Click "Use Current as BG" to capture background spectrum
7. Enable "Background Subtract" to subtract the background
8. Click "Save H5" to save current spectrum

## API Reference

### ThorlabsCCS200SpectrometerHW (Hardware Component)

#### Settings
- `int_time` (float): Integration time in seconds
- `resource_name` (str): VISA resource string
- `dll_path` (str): Path to DLL directory
- `wavelength_min` (float, read-only): Minimum wavelength
- `wavelength_max` (float, read-only): Maximum wavelength
- `n_pixels` (int, read-only): Number of pixels (3648)

#### Methods
- `acquire_spectrum()`: Acquire a new spectrum
- `get_spectrum()`: Get the most recent spectrum as numpy array
- `get_wavelengths()`: Get wavelength array as numpy array

### ThorlabsCCS200Spectrometer (Low-level Interface)

#### Attributes
- `wavelengths` (np.ndarray): Wavelength array (nm)
- `spectrum` (np.ndarray): Most recent spectrum data
- `Nspec` (int): Number of spectral pixels (3648)

#### Methods
- `set_integration_time(ms)`: Set integration time in milliseconds
- `set_integration_time_sec(sec)`: Set integration time in seconds
- `acquire_spectrum()`: Acquire and return spectrum
- `close()`: Close connection to device

### CCS200SpecLive (Measurement)

#### Settings
- `continuous` (bool): Enable continuous acquisition mode
- `save_h5` (bool): Auto-save after single-shot acquisition
- `bg_subtract` (bool): Enable background subtraction
- `baseline_subtract` (bool): Enable baseline subtraction
- `baseline_val` (float): Baseline value to subtract
- `roi_min` (float): ROI minimum wavelength (nm)
- `roi_max` (float): ROI maximum wavelength (nm)
- `roi_sum` (float, read-only): Integrated intensity in ROI

#### Methods
- `set_current_spec_as_bg()`: Capture current spectrum as background
- `save_data()`: Save current spectrum to HDF5 file

## Troubleshooting

### "Failed to initialize CCS200"
- Verify the device is connected via USB
- Check that the resource name is correct
- Ensure Thorlabs drivers are installed
- Try power cycling the device

### "Cannot load required modules"
- Verify TLCCS_64.dll is installed at the specified path
- Check that you're running 64-bit Python if using TLCCS_64.dll
- Install ScopeFoundry: `pip install ScopeFoundry`

### DLL Loading Issues
- Ensure the dll_path setting points to the correct directory
- The DLL requires other dependencies in the same directory
- Try running as administrator if permission errors occur

## Finding Your Resource Name

To find your device's VISA resource string:

1. **Using NI-VISA Interactive Control:**
   - Open NI MAX (Measurement & Automation Explorer)
   - Navigate to Devices and Interfaces
   - Look for your CCS200 under USB devices

2. **Using Thorlabs Software:**
   - Open the Thorlabs CCS software
   - The resource name is shown in the connection dialog

3. **Programmatically:**
   ```python
   import visa
   rm = visa.ResourceManager()
   print(rm.list_resources())
   ```

## License

This component follows the ScopeFoundry license structure.

## Author

Created based on the ScopeFoundry OceanOptics spectrometer component template.

## See Also

- [Thorlabs CCS200 Product Page](https://www.thorlabs.com/thorproduct.cfm?partnumber=CCS200)
- [ScopeFoundry Documentation](http://www.scopefoundry.org/)
- [OceanOptics Spectrometer Component](../oceanoptics_spec/) (similar implementation)

