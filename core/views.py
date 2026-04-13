from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

def home(request):
    return JsonResponse({
        "message": "Hello from Azure",
        "status": "ok"
    })

@require_http_methods(["GET"])
def api_users(request):
    """Get list of users"""
    users = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
        {"id": 3, "name": "Bob Johnson", "email": "bob@example.com"},
    ]
    return JsonResponse({"users": users, "count": len(users)})

@require_http_methods(["GET", "POST"])
def api_products(request):
    """Get products or create new product"""
    if request.method == "GET":
        products = [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Mouse", "price": 29.99},
            {"id": 3, "name": "Keyboard", "price": 79.99},
        ]
        return JsonResponse({"products": products})

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            new_product = {
                "id": 4,
                "name": data.get("name", "Unknown"),
                "price": data.get("price", 0)
            }
            return JsonResponse({"message": "Product created", "product": new_product}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

@require_http_methods(["GET"])
def api_product_detail(request, product_id):
    """Get a specific product by ID"""
    products = {
        1: {"id": 1, "name": "Laptop", "price": 999.99, "stock": 5},
        2: {"id": 2, "name": "Mouse", "price": 29.99, "stock": 50},
        3: {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 30},
    }

    product = products.get(product_id)
    if product:
        return JsonResponse(product)
    return JsonResponse({"error": "Product not found"}, status=404)

@require_http_methods(["GET"])
def api_stats(request):
    """Get API statistics"""
    return JsonResponse({
        "total_users": 3,
        "total_products": 3,
        "total_orders": 42,
        "version": "1.0.0",
        "environment": "Azure App Service"
    })