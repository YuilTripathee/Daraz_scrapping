<<<<<<< HEAD
# Introduction
This section is made to document test results of this project.

# Test types
    1. Load testing - Request reponse behaviour at certain requests
    2. Stress testing - Finding the number of request from where server will experience stress
    3. Performance testing - Performance of server at ceratin load

# Toolset used
| Parameters | Description |
| --- | --- |
| Name | Apache JMeter |
| Version | v4.0 - Stable release 10 - Feibruary 10 2018 |
| Developer | Apache  Software Foundation |
| Written in | Java |
| License | Apache-2.0 |

# Test result format
This is the result you could get when you configure to export by XML; and run the JMeter load test via GUI mode:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<testResults version="1.2">
<httpSample t="13" it="0" lt="13" ct="2" ts="1528269458349" s="true" lb="HTTP Request" rc="200" rm="OK" tn="Client 1-1" dt="text" by="983" sby="150" ng="1" na="1"/>
```
Here, the row format is explained in the table:
| String | Description |
| --- | --- |
| by | Bytes |
| sby | Sent Bytes |
| de | Data encoding |
| dt | Data type |
| ec | Error count |
| hn | Host name |
| it | Idle time |
| lb | Label |
| lt | Latency (time to initial response) |
| ct | Connect time |
| na | Number of active threads for all thread group |
| ng | Number of active threads in this group |
| rc | Response code |
| rm | Response message |
| s | Sucess flag |
| sc | Sample count |
| t | Elapsed time (milliseconds) |
| tn | Thread name |
| ts | Timestamp (milliseconds since midnight January 1, 1970 UTC) |
| varname | Value of named variable |

# How to run JMeter in non-GUI mode
## setup path variable
** Here is the sample method setting jmeter/bin into path: **
```s
    computer:bin user$ jmeter
    -bash: jmeter: command not found
    computer:bin user$ pwd
    /Users/user/Downloads/apache-jmeter-2.13/bin
    computer:bin user$ export PATH=$PATH:/Users/user/Downloads/apache-jmeter-2.13/bin
    computer:bin user$ jmeter
    org.apache.jmeter.testelement.TestPlan
    org.apache.jmeter.control.gui.TestPlanGui
```
Running Apache JMeter in non-GUI or non-console mode is the primary way to perform performance test on a system. For this, we have to write `something.jmx` file using GUI JMeter. It is cross platform application, you can use it anywhere. 

Below is the example of simple command which can be run to do a JMeter test:
```apache
jmeter -n -t something.jmx -l log.jtl
```
Here's the description to above arguments:

* `-n` run JMeter in non-GUI mode
* `-t` specify test plan
* `-l` specify log file name

Optional:

* `-j` name of jmeter log file
* `-r` run the test specified by jmeter property 'remote_host'
* `-R` list of remote servers, Run the test in specified remote servers
* `-H` proxy server hostname or ip address
* `-P` proxy server port

Example for optional arguments:
```apache
    jmeter -n -t my_test_plan.jmx -l log.jtl -H my.proxy.server -P 8000
```

## To generate a complete report (directly from test)
```apache
    jmeter -n -t test_plan.jmx -l jmeter.jtl -e -o results_folder
```

Arguments explained:

`-e -o [results_folder]` simply adds up a dynamic report after running a test

## To generate a complete report from existing CSV file
```apache
    jmeter -g <log file> -o <Path to output folder>
```
Arguments explained:

=======
# Introduction
This section is made to document test results of this project.

# Test types
    1. Load testing - Request reponse behaviour at certain requests
    2. Stress testing - Finding the number of request from where server will experience stress
    3. Performance testing - Performance of server at ceratin load

# Toolset used
| Parameters | Description |
| --- | --- |
| Name | Apache JMeter |
| Version | v4.0 - Stable release 10 - Feibruary 10 2018 |
| Developer | Apache  Software Foundation |
| Written in | Java |
| License | Apache-2.0 |

# Test result format
This is the result you could get when you configure to export by XML; and run the JMeter load test via GUI mode:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<testResults version="1.2">
<httpSample t="13" it="0" lt="13" ct="2" ts="1528269458349" s="true" lb="HTTP Request" rc="200" rm="OK" tn="Client 1-1" dt="text" by="983" sby="150" ng="1" na="1"/>
```
Here, the row format is explained in the table:
| String | Description |
| --- | --- |
| by | Bytes |
| sby | Sent Bytes |
| de | Data encoding |
| dt | Data type |
| ec | Error count |
| hn | Host name |
| it | Idle time |
| lb | Label |
| lt | Latency (time to initial response) |
| ct | Connect time |
| na | Number of active threads for all thread group |
| ng | Number of active threads in this group |
| rc | Response code |
| rm | Response message |
| s | Sucess flag |
| sc | Sample count |
| t | Elapsed time (milliseconds) |
| tn | Thread name |
| ts | Timestamp (milliseconds since midnight January 1, 1970 UTC) |
| varname | Value of named variable |

# How to run JMeter in non-GUI mode
## setup path variable
** Here is the sample method setting jmeter/bin into path: **
```s
    computer:bin user$ jmeter
    -bash: jmeter: command not found
    computer:bin user$ pwd
    /Users/user/Downloads/apache-jmeter-2.13/bin
    computer:bin user$ export PATH=$PATH:/Users/user/Downloads/apache-jmeter-2.13/bin
    computer:bin user$ jmeter
    org.apache.jmeter.testelement.TestPlan
    org.apache.jmeter.control.gui.TestPlanGui
```
Running Apache JMeter in non-GUI or non-console mode is the primary way to perform performance test on a system. For this, we have to write `something.jmx` file using GUI JMeter. It is cross platform application, you can use it anywhere. 

Below is the example of simple command which can be run to do a JMeter test:
```apache
jmeter -n -t something.jmx -l log.jtl
```
Here's the description to above arguments:

* `-n` run JMeter in non-GUI mode
* `-t` specify test plan
* `-l` specify log file name

Optional:

* `-j` name of jmeter log file
* `-r` run the test specified by jmeter property 'remote_host'
* `-R` list of remote servers, Run the test in specified remote servers
* `-H` proxy server hostname or ip address
* `-P` proxy server port

Example for optional arguments:
```apache
    jmeter -n -t my_test_plan.jmx -l log.jtl -H my.proxy.server -P 8000
```

## To generate a complete report (directly from test)
```apache
    jmeter -n -t test_plan.jmx -l jmeter.jtl -e -o results_folder
```

Arguments explained:

`-e -o [results_folder]` simply adds up a dynamic report after running a test

## To generate a complete report from existing CSV file
```apache
    jmeter -g <log file> -o <Path to output folder>
```
Arguments explained:

>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
`-g` arguments take a CSV log file and `-o` specifies the output folder.