


class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'visit_counted' not in request.session:
            # Increment the visit count only if the user hasn't been counted yet in this session
            request.session['visit_count'] = request.session.get('visit_count', 0) + 1
            request.session['visit_counted'] = True  # Mark the user as counted

        response = self.get_response(request)
        return response