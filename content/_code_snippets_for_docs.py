from ScopeFoundry.base_app.base_microscope_app import BaseMicroscopeApp
from ScopeFoundry.measurement import Measurement

from ScopeFoundry.logged_quantity import LoggedQuantity
from ScopeFoundry.logged_quantity.lq_circular_network import LQCircularNetwork


class LQRangeSimple(LQCircularNetwork):

    def __init__(
        self,
        min_lq: LoggedQuantity,
        max_lq: LoggedQuantity,
        center_lq: LoggedQuantity,
        span_lq: LoggedQuantity,
    ):

        self.min = min_lq
        self.max = max_lq
        self.center = center_lq
        self.span = span_lq

        lq_dict = {
            "min": self.min,
            "max": self.max,
            "center": self.center,
            "span": self.span,
        }

        LQCircularNetwork.__init__(self, lq_dict)

        self.min.add_listener(self.on_change_min_max)
        self.max.add_listener(self.on_change_min_max)
        self.center.add_listener(self.on_change_center_span)
        self.span.add_listener(self.on_change_center_span)

    # connect lqs to each other
    def on_change_min_max(self):
        mn = self.min.val
        mx = self.max.val
        span = abs(mx - mn)
        center = mn + span / 2.0
        self.update_values_synchronously(span=span, center=center)

    def on_change_center_span(self):
        span = self.span.val
        center = self.center.val
        mn = center - span / 2.0
        mx = center + span / 2.0
        self.update_values_synchronously(min=mn, max=mx)


class Measure(Measurement):

    name = "measure"

    def setup(self) -> None:

        lq = self.settings.New("X", float, initial=1.0)

        val = self.settings["X"]
        print(f"X has value {val}")

        self.settings["X"] = 2.0
        val = self.settings["X"]
        print(f"X has value {val}")

        # r = self.settings.New("radius")
        # h = self.settings.New("height")
        # v = self.settings.New("cylinder_volume")

        # def to_radius(v):
        #     r = self.settings["radius"]
        #     return r, (v / (3.1415 * r ** (1 / 2)))

        # def to_cylinder_volume(r, h):
        #     return 3.1415 * r**2 * h

        # v.connect_lq_math((r, h), to_cylinder_volume, to_radius)

        # r = self.settings.New("radius")
        # d = self.settings.New("diameter")

        # def to_radius(d):
        #     return d / 2.0
        # def to_diameter(r):
        #     return r * 2.0
        # r.connect_lq_math(d, to_radius, to_diameter)

        # r = self.settings.New("radius")
        # d = self.settings.New("diameter")

        # r.connect_lq_scale(d, 0.5)

        # min_lq = self.settings.New("X_min", initial=0)
        # max_lq = self.settings.New("X_max", initial=10)
        # center_lq = self.settings.New("X_center", initial=5)
        # span_lq = self.settings.New("X_span", initial=10)

        # self.lq_span = LQRangeSimple(min_lq, max_lq, center_lq, span_lq)

    def run(self):

        if self.settings["save_h5"]:
            # # Open a file
            # self.h5_meas_group = h5_io.h5_base_file(app=self.app, measurement=self)

            # # Create a measurement H5 group (folder) within self.h5file
            # # This stores all the measurement metadata in this group
            # self.h5_meas_group = h5_io.h5_create_measurement_group(
            #     measurement=self, h5group=self.h5_file
            # )

            # # Dump the dataset and close the file.
            # self.h5_meas_group.create_dataset(name="y", data=self.data)
            # self.h5_file.close()



        if self.settings["save_h5"]:
            self.open_new_h5_file()
            self.h5_meas_group.create_dataset(name="y", data=self.data)
            self.close_h5_file()

        if self.settings["save_h5"]:
            self.open_new_h5_file() # updates new self.h5_meas_group and self.dataset_metadata
            self.h5_meas_group.create_dataset(name="y", data=self.data)
            self.close_h5_file()

            # Save the data to a png with same file name
            import matplotlib.pyplot as plt
            plt.plot(self.data)
            plt.savefig(self.dataset_metadata.get_file_path(ext=".png"))


    def setup_figure(self):
        range = self.settings.New_Range(
            "X", include_center_span=True, include_sweep_type=True
        )

        new_widget = range.New_UI()
        self.ui = new_widget

        # self.ui = self.settings.New_UI()


class LQWidgetMicroscopeTestApp(BaseMicroscopeApp):

    name = "lq_widget_test_app"
    mdi = True

    def setup(self) -> None:

        self.add_measurement(Measure(self))


if __name__ == "__main__":
    import sys

    app = LQWidgetMicroscopeTestApp([])
    app.exec_()
