### **1. Install Homebrew (if not installed)**
Open a terminal and run:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### **2. Install Java (required for Spark)**
PySpark requires Java 8 or later. Install OpenJDK using:
```sh
brew install openjdk@11
```
Then, set up the environment variables:
```sh
echo 'export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 11)' >> ~/.zshrc
source ~/.zshrc
```

### **3. Install Apache Spark**
```sh
brew install apache-spark
```
After installation, add Spark to your environment:
```sh
echo 'export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/$(ls /opt/homebrew/Cellar/apache-spark)/libexec' >> ~/.zshrc
echo 'export PATH="$SPARK_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Verify the installation:
```sh
spark-shell
```
It should start an interactive shell.

### **4. Set Up PyCharm for PySpark**
1. Open **PyCharm** and create a new project.
2. Create a virtual environment (**venv**) in PyCharm.
3. Open the terminal in PyCharm and install PySpark:
   ```sh
   pip install pyspark
   ```
4. To test your setup, create a Python script with:
   ```python
   from pyspark.sql import SparkSession

   spark = SparkSession.builder.appName("Test").getOrCreate()
   data = [(1, "Alice", 25), (2, "Bob", 30)]
   df = spark.createDataFrame(data, ["id", "name", "age"])
   df.show()
   ```
   Run the script to check if PySpark is working correctly.
