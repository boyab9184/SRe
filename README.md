# SwissRe

This a solution for SwissRe developer assignment.

How to run the tool. There are diffent options.

1. You will need git, python3 and pip as prerequisites. Clone that github repo, install requirements and run main.py.
   ```
    mkdir Assignment_BBenev
    cd Assignment_BBenev
    git clone https://github.com/boyab9184/SwissRe.git
    cd SwissRe
    pip install -r requirements.txt
    python3 src/main.py
``` 

2. Using Docker. The tool is stateless so you should create a volume and then mount that volume when runnung the docker image. The volume acts like a folder which you can use to store and retrieve data.
   
   ```
     docker volume create bbenev-volume
   ```

   * Then inspect it:

   ```
   docker volume inspect bbenev-volume
   ```

   * Build the image and then run it:

   ```
   docker build -t bbenev-tool .
   docker run -ti -v bbenev-volume:/tool bbenev-tool
   ```

   *  At the end you can delete the volume:

    ```
    docker volume rm bbenev-volume
    ```