########################################################################
## IMPORTS
########################################################################
from kivy.lang import Builder
from typing import Union, NoReturn
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

import scripts.mdb as mdb # Importar el archivo mdb.py
from scripts.mdb import g

import sys
import threading

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

    def change_cono_vainilla(self):
        screen_manager.current = "topping_cono_vainilla"

    def change_cono_megamix(self):
        screen_manager.current = "topping_cono_megamix"

    def change_cono_chocolate(self):
        screen_manager.current = "topping_cono_chocolate"

    def change_vaso_vainilla(self):
        screen_manager.current = "topping_vaso_vainilla"

    def change_vaso_megamix(self):
        screen_manager.current = "topping_vaso_megamix"

    def change_vaso_chocolate(self):
        screen_manager.current = "topping_vaso_chocolate"
    
    def change_orden_lista_vaso_chocolate(self):
        screen_manager.current = "orden_lista_vaso_chocolate"
    
    ###################################################################
    ##### En esta funcion se crean las pantallas que se van ausar #####
    ###################################################################

    def build(self):
        # Set App Title
        self.title="E-LEGANT"
        # Set App Theme
        self.theme_cls.primary_palette='BlueGray'
        
        # Load kv screen files to builder
        screen_manager.add_widget(Builder.load_file("screens/orden_lista_vaso_chocolate.kv"))
        screen_manager.add_widget(Builder.load_file("screens/inicio.kv"))
        screen_manager.add_widget(Builder.load_file("screens/recipiente.kv"))
        screen_manager.add_widget(Builder.load_file("screens/sabor_vaso.kv"))
        screen_manager.add_widget(Builder.load_file("screens/sabor_cono.kv"))
        screen_manager.add_widget(Builder.load_file("screens/topping_cono_chocolate.kv"))
        screen_manager.add_widget(Builder.load_file("screens/topping_cono_megamix.kv"))
        screen_manager.add_widget(Builder.load_file("screens/topping_cono_vainilla.kv"))
        screen_manager.add_widget(Builder.load_file("screens/topping_vaso_chocolate.kv"))
        screen_manager.add_widget(Builder.load_file("screens/topping_vaso_megamix.kv"))
        screen_manager.add_widget(Builder.load_file("screens/topping_vaso_vainilla.kv"))
                
        # Return screen manager
        return screen_manager
    ########################################################################
    ## This function runs on app start
    ########################################################################
    #def on_start(self):
        # Delay time for splash screen before transitioning to main screen
        #Clock.schedule_once(self.change_screen1, 5) # Delay for 10 seconds
    def on_start(self) -> NoReturn:
        #Clock.schedule_once(self.generate_application_screens, 1)
        #Clock.schedule_once(self.schedule_update_total_money_label, 2)  # Programa la actualización después de un pequeño retraso
        Clock.schedule_once(self.setup_mdb, 2)
        Clock.schedule_once(self.schedule_update_total_money_label, 2)  # Programa la actualización después de un pequeño retraso

    ########################################################################
    ## This function changes the current screen to main screen
    ########################################################################
    def change_screen1(self, dt):    
        screen_manager.current = "inicio"
    def change_screen2(self, dt):    
        screen_manager.current = "inicio"
######################################################################################################
## Logica de mdb
######################################################################################################
    def setup_mdb(self, dt=None):
        port = '/dev/ttyUSB0'  # Cambia esto según tu sistema operativo
        ser = mdb.connect_to_mdb_rs232(port)
        if ser:
            mdb.enable_coin_acceptor(ser)
            mdb.enable_bill_acceptor(ser)
            print("Iniciando hilo de lectura del puerto MDB")
            mdb_thread = threading.Thread(target=mdb.mdb_read_and_parse)
            mdb_thread.daemon = True
            mdb_thread.start()
    
    def cancelar_venta(self):
        print("Cancelando venta")
        mdb.mdb_coin_change(g.total_money)
        mdb.mdb_bill_reject()
        g.total_money = 0  # Llama a la función para cancelar la venta cashless
        # self.root.current = 'recipiente'

    def schedule_update_total_money_label(self, dt):
        Clock.schedule_interval(self.update_total_money_label, 1)  # Actualiza el label cada segundo


    def update_total_money_label(self, dt):
        try:
            total_money_label = self.root.get_screen('orden_lista_vaso_chocolate').ids.total_money_label
            total_money_label.text = f"${g.total_money}"
            # amount_to_charge_label = self.root.get_screen('orden_lista_vaso_chocolate').ids.amount_to_charge_label
            # precio_helado=self.precio_pedido[0].replace("$","")
            # precio_topping=self.precio_pedido[1].replace("$","")
            # precio_helado = float(precio_helado)
            # precio_topping =float(precio_topping)
            # amount_to_charge_label.text = f"Monto a cobrar: {precio_helado + precio_topping - g.total_money} pesos" 
        except KeyError:
            print("No se pudo encontrar el ID total_money_label")
        except Exception as e:
            print(f"Error al actualizar el label: {e}")

########################################################################
## RUN APP
########################################################################      
MainApp().run()
########################################################################
## END ==>
########################################################################


















































