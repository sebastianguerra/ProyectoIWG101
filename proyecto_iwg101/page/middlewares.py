def set_next_page(get_response):

    def middleware(request):
        # Código que se ejecutará antes del llamado a la vista.
        request.INFO = {}
        if not "next" in request.GET:
            request.INFO["next"] = request.path
        else:
            request.INFO["next"] = request.GET["next"]
        
        response = get_response(request)
        # Código que se ejecutará después del llamado a la vista.
        return response

    return middleware