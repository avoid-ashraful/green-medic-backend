from rest_framework import serializers

from green_medic.apps.medicines.models import Medicine


class MedicineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'id',
            'manufacturer',
            'brand_name',
            'generic_name',
            'strength',
            'dosages',
            'price',
            'use_for'
        ]


class MedicineRetrieveSerializer(MedicineListSerializer):
    similar_medicines = serializers.SerializerMethodField()

    def get_similar_medicines(self, medicine):
        serializer = MedicineListSerializer(instance=medicine.similar_medicines, many=True)
        return serializer.data

    class Meta(MedicineListSerializer.Meta):
        fields = MedicineListSerializer.Meta.fields + [
            'dar',
            'similar_medicines',
        ]
