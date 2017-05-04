from rest_framework import serializers
from .models import Temperatura


class SerieSerializer(serializers.Serializer):
	class Meta:
        model = Temperatura
        fields = ('temp_grados_celsius','temp_grados_farenheit','humedad','presion','velocidad_viento', 'direccion', 'date')

    def create(self, validated_data):
        return Temperatura.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.temp_grados_celsius = validated_data.get('temp_grados_celsius', instance.temp_grados_celsius)
        instance.temp_grados_farenheit = validated_data.get('temp_grados_farenheit', instance.temp_grados_farenheit)
        instance.humedad = validated_data.get('humedad', instance.humedad)
        instance.presion = validated_data.get('presion', instance.presion)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.date = validated_data.get('direccion', instance.date)
        instance.save()
        return instance


 