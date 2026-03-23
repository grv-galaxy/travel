# import cloudinary
# import cloudinary.uploader
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Configure Cloudinary
# cloudinary.config(
#     cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
#     api_key=os.getenv("CLOUDINARY_API_KEY"),
#     api_secret=os.getenv("CLOUDINARY_API_SECRET"),
#     secure=True
# )

# class CloudinaryService:
#     @staticmethod
#     def upload_image(file_file, folder="general"):
#         """
#         Uploads a file to Cloudinary and returns the secure URL.
#         folder: 'fleet', 'destinations', or 'profiles'
#         """
#         try:
#             upload_result = cloudinary.uploader.upload(
#                 file_file,
#                 folder=f"indoria_vault/{folder}",
#                 resource_type="auto"
#             )
#             return upload_result.get("secure_url")
#         except Exception as e:
#             print(f"Cloudinary Upload Error: {e}")
#             return None

#     @staticmethod
#     def delete_image(public_id):
#         """Optional: Delete image if a car is removed from fleet"""
#         try:
#             cloudinary.uploader.destroy(public_id)
#             return True
#         except Exception as e:
#             print(f"Cloudinary Delete Error: {e}")
#             return False


# # Add this at the bottom of cloudinary_services.py
# def upload_image(file_file, folder="general"):
#     return CloudinaryService.upload_image(file_file, folder)












import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

class CloudinaryService:
    @staticmethod
    def upload_image(file_file, folder="general"):
        try:
            upload_result = cloudinary.uploader.upload(
                file_file,
                folder=f"indoria_vault/{folder}",
                resource_type="auto"
            )
            return upload_result.get("secure_url")
        except Exception as e:
            print(f"Cloudinary Image Upload Error: {e}")
            return None

    @staticmethod
    def upload_document(file_file, folder="user_docs"):
        try:
            upload_result = cloudinary.uploader.upload(
                file_file,
                folder=f"indoria_vault/{folder}",
                resource_type="auto", 
                use_filename=True,
                unique_filename=True
            )
            return {
                "secure_url": upload_result.get("secure_url"),
                "public_id": upload_result.get("public_id")
            }
        except Exception as e:
            print(f"Cloudinary Document Upload Error: {e}")
            return None

    @staticmethod
    def delete_resource(public_id):
        """
        Modified to handle files uploaded with resource_type='auto'
        """
        try:
            # 1. Try deleting as an image (Cloudinary classifies PDFs here under 'auto')
            result = cloudinary.uploader.destroy(public_id, resource_type="image")
            
            # 2. If not found, try deleting as 'raw' (for non-standard files)
            if result.get("result") != "ok":
                result = cloudinary.uploader.destroy(public_id, resource_type="raw")
            
            if result.get("result") == "ok":
                return True
            else:
                print(f"Cloudinary Delete Failed: {result}")
                return False
        except Exception as e:
            print(f"Cloudinary Delete Error: {e}")
            return False

# --- Helper Functions ---

def upload_image(file_file, folder="general"):
    return CloudinaryService.upload_image(file_file, folder)

def upload_document(file_file, folder="user_docs"):
    return CloudinaryService.upload_document(file_file, folder)

def delete_resource(public_id, is_document=False):
    """
    Call this from your routes: 
    delete_resource("public_id_here", is_document=True)
    """
    return CloudinaryService.delete_resource(public_id, is_document)