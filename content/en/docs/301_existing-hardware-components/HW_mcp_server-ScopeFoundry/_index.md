
---
title: HW_mcp_server (ScopeFoundry)
description: No description available.
weight: 28
---
- [GitHub Repository](https://github.com/ScopeFoundry/HW_mcp_server)
- Last Updated: 2026-02-17T21:49:35Z


#### To add to your app:

`cd to/your_project_folder/` and use the following cmd (requires [git](/docs/100_development-environment/20_git/))

```bash
git submodule add https://github.com/ScopeFoundry/HW_mcp_server ScopeFoundryHW/mcp_server
```


## Readme
# ScopeFoundry MCP Server Hardware Component

A [ScopeFoundry](https://github.com/ScopeFoundry/ScopeFoundry) HardwareComponent that provides Model Context Protocol (MCP) server functionality, enabling external tools and AI assistants to interact with ScopeFoundry applications.

## Overview

This package implements an MCP server as a ScopeFoundry HardwareComponent (`MCPServerHardware`), allowing external clients to:
- Control measurements (start/stop/status)
- Read and modify LoggedQuantity settings
- Execute Python code in both MCP thread and GUI thread contexts
- Access all ScopeFoundry app components programmatically

## Features

### MCP Tools Available

- **`list_logged_quantities`** - List all LoggedQuantity objects in the app
- **`get_logged_quantity`** - Get details of a specific LoggedQuantity
- **`set_logged_quantity`** - Modify LoggedQuantity values
- **`list_measurements`** - List all available measurements
- **`start_measurement`** - Start a specific measurement
- **`stop_measurement`** - Stop a specific measurement  
- **`get_measurement_status`** - Get measurement status and progress
- **`execute_python`** - Execute Python code in MCP server thread
- **`execute_python_gui`** - Execute Python code in main GUI thread (thread-safe)

### Thread-Safe GUI Operations

The `execute_python_gui` tool uses Qt signals/slots to safely execute GUI operations in the main thread, enabling:
- Creating PyQtGraph plots and widgets
- Modifying existing GUI elements
- Thread-safe Qt operations from external clients

## Installation

### Requirements

```bash
pip install fastmcp
pip install scopefoundry
pip install qtconsole  # For Qt support
```

### Setup

1. Copy `mcp_server_hw.py` to your ScopeFoundry project
2. Add the hardware component to your app:

```python
from mcp_server_hw import MCPServerHardware

class MyApp(BaseApp):
    def setup(self):
        # Add MCP server hardware
        self.add_hardware_component(MCPServerHardware(self))
        
        # Configure server settings
        self.hardware.mcp_server.settings['host'] = 'localhost'
        self.hardware.mcp_server.settings['port'] = 8000
```

3. Connect the hardware component in your app to start the MCP server

## Usage

### Starting the Server

The MCP server starts automatically when the hardware component connects. It serves on `http://localhost:8000/mcp` by default.

### Client Examples

#### Using FastMCP Client

```python
import asyncio
from fastmcp.client import Client

async def main():
    async with Client("http://localhost:8000/mcp") as client:
        # List available tools
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")
        
        # List measurements
        result = await client.call_tool("list_measurements", {})
        measurements = result.structured_content
        print(f"Measurements: {list(measurements.keys())}")
        
        # Start a measurement
        await client.call_tool("start_measurement", {
            "measurement_name": "my_measurement"
        })
        
        # Execute Python code
        code_result = await client.call_tool("execute_python", {
            "code": "print(f'App has {len(measurements)} measurements')"
        })
        print(f"Output: {code_result.structured_content['stdout']}")

if __name__ == "__main__":
    asyncio.run(main())
```

#### Creating GUI Elements

```python
# Create a live plot using execute_python_gui
plot_code = """
import pyqtgraph as pg
import numpy as np

# Create plot window (thread-safe in GUI thread)
plot_window = pg.PlotWidget(title="My Plot")
plot_window.setWindowTitle("ScopeFoundry Live Plot")

# Add sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
plot_window.plot(x, y, pen='cyan')

# Show window
plot_window.show()
plot_window.resize(800, 600)

# Store reference to prevent garbage collection
if not hasattr(app, '_my_plots'):
    app._my_plots = []
app._my_plots.append(plot_window)

print("Plot created successfully!")
"""

result = await client.call_tool("execute_python_gui", {"code": plot_code})
```

### Claude Code Integration

This MCP server is designed to work with [Claude Code](https://claude.ai/code), enabling AI-assisted control of ScopeFoundry applications:

```bash
# Connect Claude Code to your ScopeFoundry app
claude-code --mcp-server http://localhost:8000/mcp
```

## Testing

Run the comprehensive test suite:

```bash
python test_mcp_tools.py
```

The test suite covers:
- All MCP tool functionality
- Thread safety verification
- GUI operations with PyQtGraph
- Error handling and edge cases

### Example Test Output

```
> Testing MCPServerHardware MCP Tools via FastMCP Client
======================================================================

=== Testing tools/list ===
- Found 8 tools:
   - list_logged_quantities: List all available LoggedQuantity objects
   - get_logged_quantity: Get the value and properties of a specific LoggedQuantity
   - set_logged_quantity: Set the value of a LoggedQuantity
   - list_measurements: List all available measurements
   - start_measurement: Start a specific measurement
   - stop_measurement: Stop a specific measurement
   - get_measurement_status: Get the status of a specific measurement
   - execute_python: Execute Python code in the context of the ScopeFoundry app
   - execute_python_gui: Execute Python code in the main GUI thread

=== Testing execute_python_gui with PyQtGraph Plot ===
- PyQtGraph plot creation test:
   Creating plot in thread: MainThread
   Plot window created successfully!
   Total test plots created: 1
   Plot window visible: True
```

## Architecture

### Components

- **`MCPServerThread`** - QThread that runs the FastMCP server with its own event loop
- **`MCPServerHardware`** - ScopeFoundry HardwareComponent that manages the server thread
- **Qt Signals/Slots** - Thread-safe communication between MCP thread and GUI thread

### Thread Safety

- **MCP Thread**: Handles network requests and executes `execute_python` tool
- **GUI Thread**: Executes `execute_python_gui` tool via signal/slot mechanism
- **Synchronization**: Uses `threading.Event` for cross-thread coordination

### Data Flow

```
Client Request -> FastMCP Server -> MCP Thread -> Qt Signal -> GUI Thread -> Response
```

## Configuration

### Server Settings

- **`host`** - Server host (default: 'localhost')
- **`port`** - Server port (default: 8000)
- **`server_running`** - Read-only status indicator
- **`last_error`** - Read-only error message

### Security Considerations

- Server binds to localhost by default
- Python execution has access to full ScopeFoundry app context
- Consider network security when exposing beyond localhost

## Examples

### Live Data Visualization

Create a live FFT plot of measurement data:

```python
fft_code = """
import numpy as np
import pyqtgraph as pg
from qtpy import QtCore

# Get measurement data
meas = measurements['my_timeseries']
if meas.is_measuring() and hasattr(meas, 'buffer_h5'):
    data = meas.buffer_h5['buffer'][:]
    
    # Create FFT plot
    fft_window = pg.PlotWidget(title="Live FFT")
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data))
    
    fft_window.plot(freqs[:len(freqs)//2], 
                   np.abs(fft_data[:len(fft_data)//2]), 
                   pen='cyan')
    fft_window.show()
"""

await client.call_tool("execute_python_gui", {"code": fft_code})
```

### Automated Measurement Control

```python
# Start measurement, wait for completion, save data
control_code = """
import time

# Start measurement
measurements['my_scan'].start()
print("Measurement started")

# Monitor progress
while measurements['my_scan'].is_measuring():
    progress = measurements['my_scan'].settings['progress']
    print(f"Progress: {progress}%")
    time.sleep(1)

print("Measurement completed")
"""

await client.call_tool("execute_python", {"code": control_code})
```

## Troubleshooting

### Common Issues

1. **Server won't start**: Check that FastMCP is installed and port 8000 is available
2. **GUI operations fail**: Use `execute_python_gui` instead of `execute_python` for Qt operations
3. **Connection refused**: Ensure ScopeFoundry app is running and MCP hardware is connected

### Debug Mode

Enable debug logging in the hardware component:

```python
app.hardware.mcp_server.settings['debug_mode'] = True
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project follows the same license as ScopeFoundry.

## See Also

- [ScopeFoundry Platform](https://www.scopefoundry.org/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [Claude Code](https://claude.ai/code)
