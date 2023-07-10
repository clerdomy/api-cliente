
from rest_framework import serializers
from .models import Cliente
from .validators import *

# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validar_nome_completo(data['nome']):
            raise serializers.ValidationError({'nome':'O nome completo que você inseriu não é válido'})       
        
        if not validar_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF inserido é inválido. Verifique se o número está correto e tente novamente.'})
        else:
            data['cpf'] = ''.join(filter(str.isdigit, data['cpf']))
        return data
    
        
    def validate_rg(self, rg):
        if  len(rg) !=9:
            raise serializers.ValidationError("O RG deve conter no minimo 9 digitos")
        return rg
       