# SingleAndMultipleInheritance
Intelligent Systems
Create a python code with single and multiple inheritance, import tkinter as tk, figure out if it is from tkinter import ttk, or from tkinter import messagebox, make it about stray cats, here is a detailed info for reference: primarily Domestic Shorthair (DSH) or Domestic Longhair (DLH) cats, which are common house cats that have become feral or stray, and they come in various colors and patterns. Here's a more detailed breakdown:
Domestic Shorthair (DSH):
This is the most common type of stray cat, often referred to as a "regular house cat".
They come in a wide variety of colors and patterns, including:
Calico (black, white, and orange, mostly female)
Tortoiseshell (black and orange, mostly female)
Tuxedo (black and white)
Various other color combinations
Domestic Longhair (DLH):
Similar to DSH, but with longer fur. Feral vs. Stray:
Stray cats: were once owned and may be more likely to approach humans, while feral cats are wild and have little or no human contact.
Feral cats are often part of colonies, while stray cats are more likely to be alone.
Free-Roaming Cats:
Some cats that live primarily outdoors are referred to as "free-roaming," which can include feral, semi-feral, or stray cats.
Puspin (Pusang Pinoy):
The most common house cat in the Philippines, also known as Philippine Shorthair, Domestic Shorthair, or Housecat Shorthair internationally.
They have no specific breed and come in various coat colors and patterns.
Identifying Stray Cats:
Stray cats are often dirty or disheveled and may appear skinny or underweight.
They are usually alone, while feral cats tend to live in colonies.
Stray cats might walk and move like a house cat, while feral cats may crawl or crouch.
Stray cats might be vocal and meow, while feral cats are less likely to meow or beg.  

Key changes and explanations:

Single Inheritance:
CatCoat is a base class that holds coat-related information.
PuspinCharacteristics inherits from CatCoat, demonstrating single inheritance. This allows PuspinCharacteristics to reuse the coat attributes and methods from CatCoat and add Puspin specific information.
Multiple Inheritance:
StrayCatIdentifier inherits from both PuspinCharacteristics and CatBehavior, demonstrating multiple inheritance. This allows it to access attributes and methods from both parent classes.
Puspin Information:
The PuspinCharacteristics class now includes a puspin_info attribute and a get_puspin_info method, which displays relevant information about Puspin cats.
This information is displayed in the GUI.
Clearer Class Structure: The code is now more organized with separate classes for coat characteristics, behavior, and Puspin-specific information.
Improved GUI: Puspin info is displayed in the GUI.
Correct Super calls: Super calls are used to correctly initialize the parent classes.
Docstrings and Comments: Added comments to explain the code's functionality.

Key GUI improvements:

Window Size: self.master.geometry("450x300") sets the initial window size.
Background Color: self.master.configure(bg="#f0f0f0") sets a light gray background color for the window.
Padding: padx and pady are added to the grid layout to provide spacing between widgets.
ttk.Button: The "Identify" button is now a ttk.Button, which provides a more modern look.
Background color for labels: Added background color to labels for visual consistency.
Overall: The GUI is now more visually appealing and user-friendly.

Ontology:

@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix cat: <http://example.org/cat-ontology#> .

<http://example.org/cat-ontology> rdf:type owl:Ontology .

# Classes
cat:Cat rdf:type owl:Class .

cat:DomesticCat rdf:type owl:Class ;
    rdfs:subClassOf cat:Cat .

cat:StrayCat rdf:type owl:Class ;
    rdfs:subClassOf cat:DomesticCat .

cat:FeralCat rdf:type owl:Class ;
    rdfs:subClassOf cat:DomesticCat .

cat:FreeRoamingCat rdf:type owl:Class ;
    rdfs:subClassOf cat:DomesticCat .

cat:Puspin rdf:type owl:Class ;
    rdfs:subClassOf cat:DomesticCat .

cat:Coat rdf:type owl:Class .

cat:CoatColor rdf:type owl:Class ;
    rdfs:subClassOf cat:Coat .

cat:CoatLength rdf:type owl:Class ;
    rdfs:subClassOf cat:Coat .

cat:Behavior rdf:type owl:Class .

# Instances of CoatColor
cat:Calico rdf:type cat:CoatColor .
cat:Tortoiseshell rdf:type cat:CoatColor .
cat:Tuxedo rdf:type cat:CoatColor .
cat:Black rdf:type cat:CoatColor .
cat:White rdf:type cat:CoatColor .
cat:Gray rdf:type cat:CoatColor .
cat:Tabby rdf:type cat:CoatColor .
cat:Orange rdf:type cat:CoatColor .
cat:VariousColors rdf:type cat:CoatColor .

# Instances of CoatLength
cat:Shorthair rdf:type cat:CoatLength .
cat:Longhair rdf:type cat:CoatLength .

# Instances of Behavior
cat:ApproachesHumans rdf:type cat:Behavior .
cat:MayMeow rdf:type cat:Behavior .
cat:MovesLikeHouseCat rdf:type cat:Behavior .
cat:OftenAlone rdf:type cat:Behavior .
cat:AvoidsHumans rdf:type cat:Behavior .
cat:LessLikelyToMeow rdf:type cat:Behavior .
cat:CrawlsOrCrouches rdf:type cat:Behavior .
cat:OftenInColonies rdf:type cat:Behavior .
cat:VariedBehavior rdf:type cat:Behavior .

# Object Properties
cat:hasCoatColor rdf:type owl:ObjectProperty ;
    rdfs:domain cat:Cat ;
    rdfs:range cat:CoatColor .

cat:hasCoatLength rdf:type owl:ObjectProperty ;
    rdfs:domain cat:Cat ;
    rdfs:range cat:CoatLength .

cat:exhibitsBehavior rdf:type owl:ObjectProperty ;
    rdfs:domain cat:Cat ;
    rdfs:range cat:Behavior .

cat:isType rdf:type owl:ObjectProperty ;
    rdfs:domain cat:Cat ;
    rdfs:range cat:Cat .

# Data Properties
cat:hasPuspinInfo rdf:type owl:DatatypeProperty ;
    rdfs:domain cat:Puspin ;
    rdfs:range xsd:string .

# Example Instances
cat:ExampleStray rdf:type cat:StrayCat ;
    cat:hasCoatColor cat:Calico ;
    cat:hasCoatLength cat:Shorthair ;
    cat:exhibitsBehavior cat:ApproachesHumans , cat:MayMeow , cat:OftenAlone .

cat:ExampleFeral rdf:type cat:FeralCat ;
    cat:hasCoatColor cat:Black ;
    cat:hasCoatLength cat:Longhair ;
    cat:exhibitsBehavior cat:AvoidsHumans , cat:CrawlsOrCrouches , cat:OftenInColonies .

cat:ExamplePuspin rdf:type cat:Puspin;
    cat:hasCoatColor cat:Tabby;
    cat:hasCoatLength cat:Shorthair;
    cat:hasPuspinInfo "Common house cat in the Philippines.".

    Explanation:

Prefixes: The ontology defines prefixes for RDF, RDFS, OWL, XSD, and a custom namespace (cat).
Ontology Declaration: The owl:Ontology declaration defines the ontology itself.
Classes:
Cat, DomesticCat, StrayCat, FeralCat, FreeRoamingCat, Puspin, Coat, CoatColor, CoatLength, and Behavior classes are defined.
Subclass relationships are established using rdfs:subClassOf.
Instances:
Instances of CoatColor, CoatLength, and Behavior are created (e.g., cat:Calico, cat:Shorthair, cat:ApproachesHumans).
Example Instances of StrayCat, FeralCat, and Puspin are created.
Object Properties:
hasCoatColor, hasCoatLength, exhibitsBehavior, and isType are defined as object properties.
rdfs:domain and rdfs:range are used to specify the domain and range of each property.
Data Properties:
hasPuspinInfo is a data property to store information about Puspin cats.
Turtle Syntax: The ontology is written in Turtle (Terse RDF Triple Language) syntax, which is a human-readable format for RDF.
How to Use:

You can save this code as a .ttl file.
You can then use an RDF editor or reasoner (e.g., Protégé, Apache Jena) to load and work with the ontology.
This ontology can be used to store data about cats, and to reason about the relationships between cats, their coats, and their behaviors.
This ontology can be expanded to include more data, such as the age of the cat, the location of the cat, and the health of the cat.

Framebased Class Diagram:

classDiagram
    class CatCoat {
        - coat_colors : list
        - coat_lengths : list
        + __init__()
        + get_coat_color() : list
        + get_coat_length() : list
    }

    class CatBehavior {
        - cat_types : list
        - behavior_indicators : dict
        + __init__()
        + get_cat_types() : list
        + get_behavior_indicators(cat_type) : list
    }

    class PuspinCharacteristics {
        - puspin_info : str
        + __init__()
        + get_puspin_info() : str
    }

    class StrayCatIdentifier {
        - master : Tk
        - color_var : StringVar
        - length_var : StringVar
        - type_var : StringVar
        - color_combobox : Combobox
        - length_combobox : Combobox
        - type_combobox : Combobox
        - behavior_listbox : Listbox
        + __init__(master: Tk)
        + create_widgets()
        + update_behavior_list(event)
        + identify_cat()
    }

    CatCoat <|-- PuspinCharacteristics
    CatBehavior <|-- StrayCatIdentifier
    PuspinCharacteristics <|-- StrayCatIdentifier

    Explanation of the Class Diagram:

CatCoat:
This class represents the coat characteristics of a cat.
It has attributes for coat_colors and coat_lengths.
It provides methods to get these attributes.
CatBehavior:
This class represents the behavior of a cat.
It has attributes for cat_types and behavior_indicators.
It provides methods to get these attributes.
PuspinCharacteristics:
This class inherits from CatCoat and represents the specific characteristics of a Puspin cat.
It has an attribute for puspin_info and a method to get it.
StrayCatIdentifier:
This class inherits from both PuspinCharacteristics and CatBehavior, demonstrating multiple inheritance.
It represents the main application class.
It has attributes for the Tkinter GUI elements.
It provides methods for creating the GUI, updating the behavior list, and identifying the cat.
Relationships:
CatCoat is a parent class of PuspinCharacteristics (single inheritance).
CatBehavior and PuspinCharacteristics are parent classes of StrayCatIdentifier (multiple inheritance).
The <|-- symbol indicates inheritance (is-a relationship).
Attributes and Methods:
The diagram shows the attributes and methods of each class, along with their types.
The - symbol indicates a private attribute.
The + symbol indicates a public method.
Tkinter: The diagram also shows that the StrayCatIdentifier class interacts with tkinter elements.

![image](https://github.com/user-attachments/assets/38beb61b-9531-442c-9383-b16454f17ac9)



