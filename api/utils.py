from .serializers import *



def save_card_serialized_request_data(request, instance=None):
    if instance:
        serializer = CardSerializer(instance, data=request.data)
    else:
        serializer = CardSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

def get_card_serialized_response(request):
    board_id=Lane.objects.get(id=request.data['lane']).board.id
    cards_serialized = CardSerializer(Card.objects.filter(lane__board__id=board_id).order_by('lane_timestamp'), many=True).data
    return cards_serialized