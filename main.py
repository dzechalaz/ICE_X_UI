########################################################################
## IMPORTS
########################################################################
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

Window.fullscreen = True
########################################################################
## MAIN CLASS
########################################################################
class MainApp(MDApp):
    # Global screen manager variable
    global screen_manager
    screen_manager = ScreenManager()
    
    ########################################################################
    ## Build Function
    ########################################################################
    def restart_gif(self):
        # Reinicia la animación del GIF
        original_source = self.ids.progress.source
        self.ids.progress.source = ''  # Cambia temporalmente la fuente a vacío
        self.ids.progress.source = original_source  # Vuelve a la fuente original para reiniciar la animación

    def change_recipiente(self):
        screen_manager.current = "recipiente"

    def change_cono(self):
        screen_manager.current = "sabor_cono"

    def change_vaso(self):
        screen_manager.current = "sabor_vaso"

    def change_vainilla(self):
        screen_manager.current = "inicio"

    def change_megamix(self):
        screen_manager.current = "inicio"

    def change_chocolate(self):
        screen_manager.current = "inicio"

		

    def build(self):
        # Set App Title
        self.title="E-LEGANT"
        # Set App Theme
        self.theme_cls.primary_palette='BlueGray'
        
        # Load kv screen files to builder
        screen_manager.add_widget(Builder.load_file("screens/inicio.kv"))
        screen_manager.add_widget(Builder.load_file("screens/recipiente.kv"))
        screen_manager.add_widget(Builder.load_file("screens/sabor_vaso.kv"))
        screen_manager.add_widget(Builder.load_file("screens/sabor_cono.kv"))
        
        # Return screen manager
        return screen_manager
    ########################################################################
    ## This function runs on app start
    ########################################################################
    #def on_start(self):
        # Delay time for splash screen before transitioning to main screen
        #Clock.schedule_once(self.change_screen1, 5) # Delay for 10 seconds
        
    ########################################################################
    ## This function changes the current screen to main screen
    ########################################################################
    def change_screen1(self, dt):    
        screen_manager.current = "inicio"
    def change_screen2(self, dt):    
        screen_manager.current = "inicio"
########################################################################
## RUN APP
########################################################################      
MainApp().run()
########################################################################
## END ==>
########################################################################


















































