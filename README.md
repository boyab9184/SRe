# SwissRe

This a solution for SwissRe developer assignment.

How to run the tool? There are some different options.

1. You will need git, python3 and pip as prerequisites. Clone that repo, install requirements and run main.py.
   ```
    mkdir Assignment_BBenev
    cd Assignment_BBenev
    git clone https://github.com/boyab9184/SwissRe.git
    cd SwissRe
    pip install -r requirements.txt
    python3 src/main.py
   ``` 
    * to run tests
   ```
   python3 test/test_calculations.py
   ```

2. Using Docker. The tool is stateless so you should create a volume and then mount that volume when runnung the docker image. The volume acts like a folder which you can use to store and retrieve data.
   
   ```
   docker volume create bbenev-volume
   ```

   * Then inspect it:

   ```
   docker volume inspect bbenev-volume
   ```

   * Clone the repo and add the data file. Build the image and then run it:

   ```
   docker build -t bbenev-tool .
   docker run -ti -v bbenev-volume:/tool/outputs bbenev-tool
   ```

   * If you do not want to clone the repo, build the image from the repo and then run it.  You can use /data/test_file.csv as data file:

   ```
   docker build -t bbenev-tool https://github.com/boyab9184/SwissRe.git#main
   docker run -ti -v bbenev-volume:/tool/outputs bbenev-tool
   ```

   *  At the end you can delete the volume:

   ```
   docker volume rm bbenev-volume
   ```
