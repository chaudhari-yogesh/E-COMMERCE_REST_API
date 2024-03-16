from rest_framework import serializers


class CommonSerializerResponseView(serializers.Serializer):
    details = serializers.DictField()
    errors = serializers.ListField()
    status = serializers.IntegerField()
    timestamp = serializers.DateTimeField()


class MessageResponse(serializers.Serializer):
    
    message = serializers.CharField()


class MessageResponseSerializer(CommonSerializerResponseView):

    details = MessageResponse()

    class Meta:
        ref_name = "MessageResponseSerializer"
