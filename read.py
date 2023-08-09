"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers
"""
Importy i rozpoczęcie definicji UserSerializer:

Importujemy moduły get_user_model oraz serializers z
biblioteki Django REST framework. Rozpoczynamy
definicję klasy UserSerializer,
która będzie służyć do serializacji użytkowników.
"""
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the user object.
    Definicja Meta wewnątrz klasy:

Wewnątrz klasy UserSerializer definiujemy klasę Meta,
 która zawiera dodatkowe metadane dla serializera.
    """
    class Meta:
        """
        Meta class defining the serializer's behavior.
        Definicja modelu w klasie Meta:

W atrybucie model klasy Meta wskazujemy model, na którym oparty będzie nasz serializer. W tym przypadku używamy funkcji get_user_model() z Django,
która zwraca model użytkownika, dostosowany do bieżącej konfiguracji.
Definicja pól w klasie Meta:

W atrybucie fields klasy Meta wskazujemy, które pola z modelu chcemy uwzględnić
w serializacji. Tutaj wskazujemy 'email', 'password' i 'name'.
        """
        # Wskazujemy model, na którym będzie bazować serializer
        model = get_user_model()

        # Wskazujemy pola modelu, które mają być uwzględnione w serializacji
        fields = ['email', 'password', 'name']

        # Definiujemy dodatkowe atrybuty dla poszczególnych pól, np. hasła
        """
Dodatkowe atrybuty pól w klasie Meta:
W atrybucie extra_kwargs klasy Meta definiujemy dodatkowe atrybuty dla poszczególnych pól.
Dla przykładu, dla pola 'password' ustawiamy write_only na True, co oznacza, że pole to nie będzie uwzględniane przy deserializacji.
Dodatkowo ustawiamy minimalną długość hasła na 5 znaków.
        """
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """
        Custom method to create a user with encrypted password.
        Metoda create wewnątrz klasy UserSerializer:
Definiujemy własną metodę create, która tworzy nowego użytkownika z zaszyfrowanym hasłem.
Wykorzystujemy manager modelu użytkownika,
aby stworzyć nowego użytkownika na podstawie zweryfikowanych danych.
        """
        # Wykorzystujemy manager modelu User, aby utworzyć nowego użytkownika
        return get_user_model().objects.create_user(**validated_data)
