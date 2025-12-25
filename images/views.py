from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ImportedImage


@api_view(['POST'])
def import_google_drive(request):
    folder_url = request.data.get('folder_url')

    # MOCK LOGIC (Explain Google Drive API in interview)
    image = ImportedImage.objects.create(
        name="sample.jpg",
        google_drive_id="123abc",
        size=102400,
        mime_type="image/jpeg",
        storage_path="https://s3.amazonaws.com/bucket/sample.jpg"
    )

    return Response({"message": "Import started"})

@api_view(['GET'])
def list_images(request):
    images = ImportedImage.objects.all().values()
    return Response(images)
