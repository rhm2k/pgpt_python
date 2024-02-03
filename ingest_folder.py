# 2024-02-01 v 0.01 ai-assist 
from pgpt_python.client import PrivateGPTApi
import os

# Initialize the PrivateGPT API client
client = PrivateGPTApi(base_url="http://your_privategpt_url_here")

def ingest_files(directory_path):
    """
    Ingest files from the given directory into PrivateGPT and retain a map of file names to document IDs.
    
    :param directory_path: Path to the directory containing files to ingest.
    :return: Dictionary with file names as keys and document IDs as values.
    """
    files_doc_ids = {}
    
    # Iterate over each file in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        
        # Ensure we're working with a file
        if os.path.isfile(file_path):
            # Open the file and read its content
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            # Ingest the file content into PrivateGPT
            response = client.ingestion.ingest_document(content=file_content)
            
            # Store the file name and the returned doc ID in the dictionary
            doc_id = response['doc_id']  # Adjust based on actual response structure
            files_doc_ids[file_name] = doc_id
    
    return files_doc_ids

# Example usage
directory_path = '/path/to/your/files'
ingested_files_doc_ids = ingest_files(directory_path)
print(ingested_files_doc_ids)
