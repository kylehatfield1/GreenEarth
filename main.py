# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 14:41:59 2022

@author: Kyle Hatfield
"""
import xmlschema

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty

import kivymd
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.menu import MDDropdownMenu

from MetalsRecord import MetalsRecord

kv = '''   
  
WindowManager:
    NewCustomerCheckScreen:
    NewCustomerRegistration:
    ExistingCustomer:
    PrintCashCard:
    AddMetals:
    

<NewCustomerCheckScreen>:
    name: "CustomerCheck"

    MDTopAppBar:
        title: "Green Earth - Scale"
        pos_hint: {"top": 1}
                       
    MDCard:
        id: display
        orientation: "vertical"
        size_hint: (0.87, 0.78)
        pos_hint: {"center_x": .5, "center_y": .45}
    
        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                size_hint_y: .3
                font_style: "H6"
                text: "New or existing customer?"
            MDBoxLayout:
                spacing: 15
                padding: 15

                MDRaisedButton:
                    text: "New Customer"
                    halign: 'center'
                    on_release:
                        app.root.current = "NewCustomer"
                        root.manager.transition.direction = "left"

                MDRaisedButton:
                    text: "Existing Customer"
                    halign: 'center'
                    on_release:
                        app.root.current = "ExistingCustomer"
                        root.manager.transition.direction = "left"

                MDRaisedButton:
                    text: "Add Metals"
                    halign: 'center'
                    on_release:
                        app.root.current = "AddMetals"
                        root.manager.transition.direction = "left"
        
        
<NewCustomerRegistration>:
    name: "NewCustomer"    

    MDTopAppBar:
        title: "Green Earth - Scale"
        pos_hint: {"top": 1}
                       
    MDCard:
        id: display
        orientation: "vertical"
        size_hint: (0.87, 0.78)
        pos_hint: {"center_x": .5, "center_y": .45}
        #padding: 25
        #spacing: 15

        MDLabel:
            size_hint_y: .2
            text: "New customer Registration"

        MDBoxLayout:
            #padding: 15
            #spacing: 35         
            #size_hint_y: .1


            MDGridLayout:
                row_force_default: True
                row_default_height: 50
                #padding: 35
                #spacing: 5
                #pos_hint: {"top": 1}
                #size_hint_y: .1
                cols: 1

                MDLabel:
                    text: "Customer Information"
            
                MDTextField:
                    id: FirstName
                    hint_text: "First Name"

                MDTextField:
                    id: MiddleName
                    hint_text: "Middle Name"

                MDTextField:
                    id: LastName
                    hint_text: "Last Name"

                MDTextField:
                    id: LicenseNumber
                    hint_text: "Drivers License Number"

                MDTextField:
                    id: LicenseState
                    hint_text: "Drivers License State"

                MDTextField:
                    id: Street
                    hint_text: "Street Address"

                MDTextField:
                    id: City
                    hint_text: "City"

                MDTextField:
                    id: Zip
                    hint_text: "Zip"


            MDGridLayout:
                cols: 1

                MDLabel:
                    text: "Vehicle Information"

                MDTextField:
                    id: Make
                    hint_text: "Make"    

                MDTextField:
                    id: Model
                    hint_text: "Model"


        MDBoxLayout:
            #spacing: "35dp"
            #padding: "65dp"
            
            MDRaisedButton:
                text: "Back"
                halign: 'center'
                on_release:
                    app.root.current = "CustomerCheck"
                    root.manager.transition.direction = "right"

            MDRaisedButton:
                text: "Done"
                halign: 'center'
                on_release:
                    app.root.current = "ExistingCustomer"
                    root.manager.transition.direction = "left"


<ExistingCustomer>:
    name: "ExistingCustomer"    

    MDTopAppBar:
        title: "Green Earth - Scale"
        pos_hint: {"top": 1}
                       
    MDCard:
        id: display
        orientation: "vertical"
        size_hint: (0.87, 0.78)
        pos_hint: {"center_x": .5, "center_y": .45}
    
        MDBoxLayout:
            size_hint_y: .3

            MDLabel:
                text: "Existing Customer"

        MDBoxLayout:
            spacing: "35dp"
            padding: "65dp"
            
            MDRaisedButton:
                text: "Back"
                halign: 'center'
                on_release:
                    app.root.current = "CustomerCheck"
                    root.manager.transition.direction = "right"

            MDRaisedButton:
                text: "Print"
                halign: 'center'
                on_release:
                    app.root.current = "PrintCashCard"
                    root.manager.transition.direction = "left"  

            MDRaisedButton:
                text: "Enter Metals"
                halign: 'center'
                on_release:
                    app.root.current = "EnterMetals"
                    root.manager.transition.direction = "left" 

<PrintCashCard>:
    name: "PrintCashCard"    

    MDTopAppBar:
        title: "Green Earth - Scale"
        pos_hint: {"top": 1}
                       
    MDCard:
        id: display
        orientation: "vertical"
        size_hint: (0.87, 0.78)
        pos_hint: {"center_x": .5, "center_y": .45}
    
        MDBoxLayout:
            size_hint_y: .3
            spacing: "35dp"
            padding: "15dp"

            MDLabel:
                text: "Print Cash Card"

        MDBoxLayout:
            size_hint_y: .3
            spacing: "35dp"
            padding: "65dp"
            
            MDRaisedButton:
                text: "Back"
                halign: 'center'
                on_release:
                    app.root.current = "ExistingCustomer"
                    root.manager.transition.direction = "right"

<AddMetals>:
    name: "AddMetals"    

    MDTopAppBar:
        title: "Green Earth - Scale"
        pos_hint: {"top": 1}
                       
    MDCard:
        id: display
        orientation: "vertical"
        size_hint: (0.87, 0.78)
        pos_hint: {"center_x": .5, "center_y": .45}
        
        MDBoxLayout:
            orientation: "vertical"
            spacing: 15
            padding: 15
            MDLabel:
                size_hint_y: .3
                font_style: "H6"
                text: "Add Metal Types"

            MDDropDownItem:
                id: primaryMetalMenu
                #pos_hint: {'center_x': .5, 'center_y': .5}
                text: 'Select Primary Metal Type'
                on_release: root.primaryMetalMenu.open()
            MDDropDownItem:
                id: secondaryMetalMenu
                #pos_hint: {'center_x': .5, 'center_y': .4}
                text: 'Select Secondary Metal Type'
                on_release: root.secondaryMetalMenu.open() if root.bShowSecondaryTypes else None
            MDTextField:
                size_hint_x: .3
                id: priceInput
                hint_text: "Price"
                input_filter: 'float'
 
        MDBoxLayout:
            size_hint_y: .3
            MDRaisedButton:
                text: "Add Metal"
                on_release: root.addMetal()

            MDRaisedButton:
                text: "Remove Metal"
                on_release: root.removeMetal()

        MDBoxLayout:
            orientation: "vertical"
            MDScrollView:
                MDSelectionList:
                    id: metalList

            MDRaisedButton:
                text: "Back"
                halign: 'center'
                on_release:
                    app.root.current = "CustomerCheck"
                    root.manager.transition.direction = "right"  
                                   
                               
    '''

class ListItem(OneLineListItem):
    icon = StringProperty()

def GetMetalTypes():
    metalTypes = GetMetalStringLiterals()
    metalTypes_dict = ParseMetalTypes(metalTypes)

    return metalTypes_dict


def GetMetalStringLiterals():
    path = r"Data/XML_Files/MetalTypeForm.xsd"
    schema = xmlschema.XMLSchema(path)
    components = []
    for xsd_component in schema.iter_components():
        components.append(xsd_component)
    metalTypes = components[2].enumeration
    
    return metalTypes


def ParseMetalTypes(metalTypes):
    metalTypes_dict = {}
    for metalType in metalTypes:
        primaryDone = False
        primaryType = ""
        secondaryType = ""
        for char in metalType:
            if not char == '-' and not primaryDone:
                primaryType += char
            elif char == '-' and not primaryDone:
                primaryDone = True
            elif not char == '-' and primaryDone:
                secondaryType += char
        if primaryType in metalTypes_dict:
            metalTypes_dict[primaryType].append(secondaryType)
        else:
            metalTypes_dict[primaryType] = [secondaryType]
            
    return metalTypes_dict

class NewCustomerCheckScreen(Screen):
    pass

class NewCustomerRegistration(Screen):
    pass

class ExistingCustomer(Screen):
    pass

class PrintCashCard(Screen):
    pass

class AddMetals(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.primaryMetalType = None
        self.secondaryMetalType = None
        self.listBuilt = False
        self.widgets = {}

    def buildSecondaryMenu(self):
        #self.ids.secondaryMetalMenu.opacity = 1
        metalTypes = GetMetalTypes()
        primaryType = self.primaryMetalType
        secondaryTypes = metalTypes[primaryType]
        menu_items = [
            {
                "viewclass": "ListItem",
                "text": f"{secondaryType}",
                "height": dp(56),
                "on_release": lambda x = f"{secondaryType}": self.setSecondaryType(x),
            } for secondaryType in secondaryTypes
        ]
        self.secondaryMetalMenu = MDDropdownMenu(
            caller=self.ids.secondaryMetalMenu,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.secondaryMetalMenu.bind()
        
    
    def updateSecondaryTypes(self):
        #self.secondaryMetalMenu.text = 'Select Secondary Metal Type'
        self.ids.secondaryMetalMenu.set_item('Select Secondary Metal Type') 
        self.secondaryMetalType = None
        metalTypes = GetMetalTypes()
        secondaryTypes = metalTypes[self.primaryMetalType]
        menu_items = [
            {
                "viewclass": "ListItem",
                "text": f"{secondaryType}",
                "height": dp(56),
                "on_release": lambda x = f"{secondaryType}": self.setSecondaryType(x),
            } for secondaryType in secondaryTypes
        ]
        self.secondaryMetalMenu.items = menu_items
        self.secondaryMetalMenu.bind()
    

    def setPrimaryType(self, text_item):
        self.ids.primaryMetalMenu.set_item(text_item)
        self.primaryMetalType = text_item
        if not self.bShowSecondaryTypes:
            self.bShowSecondaryTypes = True
            self.buildSecondaryMenu()
        else:
            self.updateSecondaryTypes()
        self.primaryMetalMenu.dismiss()


    def setSecondaryType(self, text_item):
        self.ids.secondaryMetalMenu.set_item(text_item)
        self.secondaryMetalType = text_item
        self.secondaryMetalMenu.dismiss()
    
    def on_enter(self):
        self.bShowSecondaryTypes = False
        self.metalsRecord = MetalsRecord()
        if not self.listBuilt:
            self.listBuilt = True
            for index in self.metalsRecord.MetalsRecordDF.index:
                if index == 'init':
                    continue
                price = self.metalsRecord.MetalsRecordDF.loc[index]['price']
                listText = f"{str(index)}     Price: $ {str(price)}"
                listItem = OneLineListItem(text=listText)
                self.ids.metalList.add_widget(listItem)
        metalTypes = GetMetalTypes()
        primaryTypes = []
        for key in metalTypes.keys():
            primaryTypes.append(str(key))
        menu_items = [
            {
                "viewclass": "ListItem",
                "text": f"{primaryType}",
                "height": dp(56),
                "on_release": lambda x = f"{primaryType}": self.setPrimaryType(x),
            } for primaryType in primaryTypes
        ]
        self.primaryMetalMenu = MDDropdownMenu(
            caller=self.ids.primaryMetalMenu,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        
        self.primaryMetalMenu.bind()  

    def addMetal(self):
        if self.primaryMetalType == None or self.secondaryMetalType == None or self.ids.priceInput.text == '':
            return
        price = self.ids.priceInput.text
        #print(str(price))
        #price = 0.23
        metalType = f"{self.primaryMetalType} - {self.secondaryMetalType}"
        listText = f"{self.primaryMetalType} - {self.secondaryMetalType}     Price: $ {str(price)}"
        if metalType in self.metalsRecord.MetalsRecordDF.index:
            return
        self.metalsRecord.AddRecord(metalType, price)
        listItem = OneLineListItem(text=listText)
        self.ids.metalList.add_widget(listItem)
        self.widgets[listText] = ListItem


    def removeMetal(self):
        pass


class WindowManager(ScreenManager):
    pass


class TruckScaleApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        self.root = Builder.load_string(kv)
        root = self.root
        
    
if __name__ == '__main__':
    TruckScaleApp().run()
