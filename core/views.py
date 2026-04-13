from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from core.models import Product
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
        products = Product.objects.all()
        products_list = []
        for product in products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "price": str(product.price),
                "description": product.description,
                "image": product.image.url if product.image else None,
                "created_at": product.created_at.isoformat()
            }
            products_list.append(product_data)
        return JsonResponse({"products": products_list, "count": len(products_list)})

    elif request.method == "POST":
        try:
            name = request.POST.get("name")
            price = request.POST.get("price")
            description = request.POST.get("description", "")
            image = request.FILES.get("image")

            if not name or not price:
                return JsonResponse({"error": "Name and price are required"}, status=400)

            product = Product.objects.create(
                name=name,
                price=price,
                description=description,
                image=image
            )
            return JsonResponse({
                "message": "Product created successfully",
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": str(product.price),
                    "image": product.image.url if product.image else None
                }
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@require_http_methods(["GET"])
def api_product_detail(request, product_id):
    """Get a specific product by ID"""
    try:
        product = Product.objects.get(id=product_id)
        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "description": product.description,
            "image": product.image.url if product.image else None,
            "created_at": product.created_at.isoformat(),
            "updated_at": product.updated_at.isoformat()
        })
    except Product.DoesNotExist:
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