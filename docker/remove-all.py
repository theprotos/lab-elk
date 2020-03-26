import subprocess
import time

start_time = time.time()

containers = subprocess.getoutput(['docker', 'ps', '-a', '-q'])
#containers = containers.replace('\n', ' ')
images = subprocess.getoutput(['docker', 'images', '-q'])
#images = images.replace('\n', ' ')

if containers:
    print("Stop and remove all contaners: ")
    for container in containers.split():
        subprocess.call(["docker", "stop", container])
        subprocess.call(["docker", "rm", "-f", container])
else:
    print("No containers")

if images:
    print("Remove all images: ")
    for image in images.split():
        print(image)
        subprocess.call(["docker", "rmi", "-f", image])
else:
    print("No images")
print("\n--- %s seconds ---" % (time.time() - start_time))
