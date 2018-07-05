<<<<<<< HEAD
# check if those files are previously present and remove them
if [ results ]
then
    rm -r results
fi

if [ jmeter.jtl ]
then
    rm jmeter.jtl
fi
#run the test
jmeter -n -t Daraz_scrapping.jmx -l jmeter.jtl -e -o results
=======
# check if those files are previously present and remove them
if [ results ]
then
    rm -r results
fi

if [ jmeter.jtl ]
then
    rm jmeter.jtl
fi
#run the test
jmeter -n -t Daraz_scrapping.jmx -l jmeter.jtl -e -o results
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
