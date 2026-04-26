import shutil
import os

def copy_static():
    source_dir = os.path.join(os.getcwd(), 'static')
    destination_dir = os.path.join(os.getcwd(), 'docs')

    delete_dir_contents(destination_dir)

    copy_contents(source_dir, destination_dir)


def copy_contents(source_dir, destination_dir):
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
        else:
            os.makedirs(destination_path, exist_ok=True)
            copy_contents(source_path, destination_path)


def delete_dir_contents(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            if os.path.isfile(item_path):
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)
    else:
        print(f"Warning: Directory '{directory}' does not exist. Skipping.")
