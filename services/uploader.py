class Uploader:

    @staticmethod
    def upload_photo_partniors(instance, filename):
        return f"partniors/{filename}"
    
    @staticmethod
    def upload_photo_products(instance, filename):
        return f"products/{filename}"
    
    @staticmethod
    def upload_photo_to_blog(instance, filename):
        return f"products/{filename}"
    
