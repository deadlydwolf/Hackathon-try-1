#GEO Location
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import gps

class EmergencyContactApp(App):
    def build(self):
        self.location_label = Label(text="Location: Not available")
        self.get_location_button = Button(text="Get Location", on_press=self.get_location)
        self.send_location_button = Button(text="Send Location to First Responder", on_press=self.send_location)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.location_label)
        layout.add_widget(self.get_location_button)
        layout.add_widget(self.send_location_button)

        return layout

    def get_location(self, instance):
        gps.configure(on_location=self.on_location)
        gps.start(minTime=1000, minDistance=1)

    def on_location(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']
        self.location_label.text = f"Location: Latitude - {lat}, Longitude - {lon}"

    def send_location(self, instance):
        # Code to send location to first responder (API call, etc.)
        pass

if __name__ == '_main_':
    EmergencyContactApp().run()
