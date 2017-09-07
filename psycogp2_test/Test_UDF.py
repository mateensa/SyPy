import psycopg2;
retval ="";
try:
	con=psycopg2.connect("dbname=dwa user=integration_user host=xxxxxx.cmj8jk61oxi0.us-west-2.redshift.amazonaws.com password= port=5439");
	retval = "I am able to connect to the database";
except:
    retval = "---->I am unable to connect to the database";

print(retval)
