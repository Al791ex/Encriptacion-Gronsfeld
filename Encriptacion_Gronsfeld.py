"""
Aplicación que simule el Método de Encriptación de Gronsfeld.

La interfaz de Entrada deberá solicitar los siguientes argumentos:

 - Frase a ser codificada
 - Clave de Cifrado
La interfaz de salida presentara el resultado de la Frase Codificada al igual que la Frase Sin Codificar y Clave de Cifrado.
"""
from flet import *

def main (page: Page):
    page.title = "Gronsfeld"
    page.theme_mode = ThemeMode.LIGHT
    page.window_width= 900
    page.window_height = 700
    page.padding = 20
    
    # confirm dialog
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()
    
    page.window_prevent_close = True
    page.on_window_event = window_event
    
    def si_click(e):
        page.window_destroy()
    
    def no_click(e):
        confirm_dialog.open = False
        page.update()
        
    confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Confirmación"),
        content=Text("¿Quieres salir?"),
        actions=[
            ElevatedButton("Si", on_click= si_click),
            OutlinedButton("No", on_click= no_click)
        ],
        actions_alignment=MainAxisAlignment.END
    )
    
    # Algoritmo de encriptacion
    def encriptar_frase(e):
        frase = frase_field.value
        clave = clave_field.value
        
        frase_encriptada_text.value = ""
        frase_text.value = ""
        clave_text.value = ""
        
        Alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
        Encript=""
        vez=0
        
        status_frase = False
        status_clave = False
        
        if frase == "":
            
            frase_field.error_text = "No puedes dejar campos sin rellenar"
            status_frase = False
            page.update()
        else:
            
            frase_field.error_text = None
            status_frase = True
            page.update()
            
        if clave.isdigit():
            
            clave_field.error_text = None
            status_clave = True
            page.update()    
        elif clave == "":
            
            clave_field.error_text = "No puedes dejar campos sin rellenar"
            status_clave = False
            page.update()  
        else:
            
            clave_field.error_text = "Solo se permiten caracteres numericos"
            clave_field.value = ""
            status_clave = False
            page.update()
    
        if status_clave and status_frase:
            for x in frase:
                if(vez>len(clave)-1):
                    vez=0
                if(vez<len(clave)):
                    mov=int(clave[vez])
                if(x.isalpha()):
                    vez=vez+1 
                    pos=Alfabeto.index(x.lower())+mov
                    if(pos>=len(Alfabeto)):
                        pos=pos-len(Alfabeto)
                    Encript=Encript+Alfabeto[pos]
                else:
                    Encript=Encript+x

            frase_encriptada_text.value = Encript
            frase_text.value = frase
            clave_text.value = clave
            
            frase_field.value = ""
            clave_field.value = ""
            page.update()
    
    #Entradas
    frase_field = TextField(label="Frase", multiline=True, min_lines=1, max_lines=3)
    clave_field = TextField(label="Clave de cifrado")
    button = Text("Encriptar", font_family="monserrat", size=25, text_align=TextAlign.CENTER)
    
    #Salidas
    frase_text = Text(" ", size=18, text_align=TextAlign.CENTER)
    clave_text = Text(" ", size=18, text_align=TextAlign.CENTER)
    frase_encriptada_text = Text(" ", size=18, text_align=TextAlign.CENTER)
    # Controls
    page.add(
        Column(
            controls=[
                Container(
                    content=Text("Encriptación de Gronsfeld", font_family="monserrat", text_align=TextAlign.CENTER, size=40),
                    bgcolor=colors.SURFACE_VARIANT, 
                    width=float("inf"),
                    border_radius=15
                ),
                Text("Ingresa los datos:", font_family="monserrat", size= 25),
                Row(
                    controls=[
                        frase_field,
                        clave_field,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=30
                ),
                ElevatedButton(content=button, on_click= encriptar_frase, width=700, height=50, color=colors.BLACK),
                Divider(),

                #Salida
                Row(
                    controls=[
                        #Frase a encriptar
                        Column(
                            controls=[
                                Text("Frase a encriptar 💬", font_family="monserrat", size= 25, width=250, text_align=TextAlign.CENTER),
                                Container(content=frase_text, bgcolor= colors.AMBER, width= 250, border_radius=15, border=border.all(15,colors.AMBER))
                            ],
                            spacing=15   
                        ),
                        
                        #Clave de cifrado
                        Column(
                            controls=[
                                Text("Clave de cifrado 🔑", font_family="monserrat", size= 25, width=250, text_align=TextAlign.CENTER),
                                Container(content=clave_text, bgcolor= colors.AMBER, width= 250, border_radius=15, border=border.all(15,colors.AMBER))
                            ],
                            spacing=15  
                        ),
                        
                        #Frase encriptada
                        Column(
                            controls=[
                                Text("Frase encriptada 🔒", font_family="monserrat", size= 25, width=250, text_align=TextAlign.CENTER),
                                Container(content=frase_encriptada_text, bgcolor= colors.AMBER, width= 250, border_radius=15, border=border.all(15,colors.AMBER))
                            ]    
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=30
                )
            ], #ojo esto no funciona, arreglalo si puedes
            horizontal_alignment=CrossAxisAlignment.CENTER,    
            spacing=40
        )
    )
    page.update()
    
app(target=main)
