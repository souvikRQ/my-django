from django.http import JsonResponse
from django.db import connection
import json

def health_view(request):
    return JsonResponse({"message": "Welcome to the Python Django + PostgreSQL API!"})

def status_view(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW()")
            row = cursor.fetchone()
        return JsonResponse({
            "status": "Database connected",
            "timestamp": row[0],
        })
    except Exception as e:
        return JsonResponse({
            "status": "Database connection failed",
            "error": str(e),
        }, status=500)

def dummy_view(request):
    data = [
        {
            "id": 1,
            "name": "Dummy Item 1",
            "description": "This is a dummy item from the API",
        },
        {
            "id": 2,
            "name": "Dummy Item 2",
            "description": "This is another dummy item",
        },
    ]
    return JsonResponse(data, safe=False)

def users_view(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            columns = [col[0] for col in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return JsonResponse(rows, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
