import csv, sys, os, errno
import datetime, time

ops3pdgs_password='4hbvFjW8S2yBIU+GDDR3tyULfqOy//LFSC+y+97dLpDjnHiWVxPusfBemJ/6fj0cYXWreb6MVoXyCyag4OGxmYLPS9Ldiwkvyxav9gFPy1ck81pxn2/GmiJ8qLGkb8gyRx4rA+ixeKRUgNksGYtOjQQH0yiHcpDz1By/arG1L0s='
s3pdgs_password='BkBW4F3jwTMkMflLhqm0xoR1onwpgcy0ECgl71woUU9CDTOrvOT5QD5Vuy421A5ZM7rno4wGW4K3AkGtp0iAr6JN0ajOK3F2g96jWA/GMM6JyiAH7IvMt49cR/bz6cIxvhMlL0TjQoPKPVnehlUApGB6dc0uv8q4pRCIRdLu2lA='
s3sysadm_password='00XBUqCqcIleuWg9kHpq0oouE7W2NB4W5RSd5j+9Rsx8pY9ojuXfT3IfnTaOgwXx70+8JZaMzentURP8kDpPtUQgvsfWtI8iTd3XrQduPFZVLt/OABy0RYSOkmkgihKs0OY+I0tKBpND0wUXiy39/TVoxW00oZHDoRTMwpLIPL4='
s3mpfuser_password='bGgWWNlOOLCqBTX3VOrpMSsg8z3eS3wdoEHpQ4W7jE8OdYvYjqsgiNiDB1wEDgr8DeN5209ObV64tUTlcv83GPqFYssxdn13I8IAtd74AP7/dn22diPKzizJlcVWZdk/Eut76krshkPHo+TC17FclGHy8EJivdExgQq3da2Ux7Q='
GEMS_ftp_password='XlcbD2EGp+TKslUlftx/rFt1GKVGJgs2dGAMhTbtB2TdrT0172R5D5S41XoIqz0S4VAlYNwNRoJc0l8iQvjAxptrHbmeo+Af2QXznbusRVOynYlgxQiPvG2Ccw9XjUDs708YJXRPidSAb4UUouXVGFNLFOE1NPasJ69shQ7eAns='


def createDir(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def removeDir(path):
    if os.path.exists(os.path.dirname(path)):
        print 'OLD DIRECTORY FOUND...'
        print 'REMOVING OLD DIRECTORY!'
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

numParameters = len(sys.argv)
cmdargs = str(sys.argv)
filename = ''

OUTPUT_DIR = 'output/'

src_password=''
dest_password=''

if numParameters > 2:
    print 'Too many arguments, please type generator.py --help for instructions!'
    exit(-1)

if numParameters == 2 and '--help' in cmdargs:
    print '\t generator.py --help this help'
    print '\t generator.py <input_file>.csv'
    exit(0)

if '.csv' not in cmdargs and numParameters == 2:
    print 'Please spefify a valid csv file!'
    exit(0)

if numParameters == 1:
    print 'Please type --help for commands'
    exit(0)

filename = sys.argv[1]

removeDir(OUTPUT_DIR)

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        print 'Generating Policies...'
        count = 0
        for row in reader:
            tokens = row[0].split(';')
            
            if count > 0:
                policy_id = tokens[0]
                if not policy_id:
                    print '[WARNING]: ID empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                fromcomponent = tokens[1]
                if not fromcomponent:
                    print '[WARNING]: Component From empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                fromcenter = tokens[2]
                if not fromcenter:
                    print '[WARNING]: Center From empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                fromplatform = tokens[3]
                if not fromplatform:
                    print '[WARNING]: Platform From empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                tocomponent = tokens[4]
                if not tocomponent:
                    print '[WARNING]: Component To empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                tocenter = tokens[5]
                if not tocenter:
                    print '[WARNING]: Center To empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                toplatform = tokens[6]
                if not toplatform:
                    print '[WARNING]: Platform To empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                policyversion = tokens[7]
                if not policyversion:
                    print '[WARNING]: Policy Version empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                enabled = tokens[8]
                if not enabled:
                    print '[WARNING]: Enabled empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                datatype = tokens[9]
                if not datatype:
                    print '[WARNING]: Data Type empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                regex = tokens[10]
                if not regex:
                    print '[WARNING]: Regex empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                installationnode = tokens[11]
                if not installationnode:
                    print '[WARNING]: Installation Mode empty ad line ',(count)
                    exit(-1)
                src_user = tokens[12]
                if not src_user:
                    print '[WARNING]: SRC User empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                src_host = tokens[13]
                if not src_host:
                    print '[WARNING]: SRC Host empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                src_path = tokens[14]
                if not src_path:
                    print '[WARNING]: SRC Path empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                src_protocol = tokens[15]
                if not src_protocol:
                    print '[WARNING]: SRC Protocol empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                dest_user = tokens[16]
                if not dest_user:
                    print '[WARNING]: Dest User empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                dest_host = tokens[17]
                if not dest_host:
                    print '[WARNING]: Dest Host empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                dest_path = tokens[18]
                if not dest_path:
                    print '[WARNING]: Dest PATH empty ad line ',(count)
                    print 'Execution will be STOPPED!'
                    exit(-1)
                dest_protocol = tokens[19]
                if not dest_protocol:
                    print '[WARNING]: Dest Protocol empty ad line ',(count)
                    print 'Execution will be STOPPED!'                
                    exit(-1)
                suffixprefix = tokens[20]
                if not suffixprefix:
                    print '[WARNING]: Suffix - Prefix empty ad line ',(count)
                    #print 'Execution will be STOPPED!'
                    #exit(-1)

                if src_user in 'ops3pdgs' :
	                src_password = ops3pdgs_password

                if src_user in 's3sysadm' :
	                src_password = s3sysadm_password

                if src_user in 's3mpfuser':
	                src_password = s3mpfuser_password

                if src_user in 's3pdgs':
	                src_password = s3pdgs_password

                if src_user in 'GEMS_ftp':
	                src_password = GEMS_ftp_password

                if dest_user in 'ops3pdgs':
                    dest_password = ops3pdgs_password

                if dest_user in 's3sysadm':
                    dest_password = s3sysadm_password

                if dest_user in 's3mpfuser':
                    dest_password = s3mpfuser_password

                if dest_user in 's3pdgs':
                    dest_password = s3pdgs_password

                if dest_user in 'GEMS_ftp' :
                    dest_password = GEMS_ftp_password
                
                
                
                directory = OUTPUT_DIR+fromcenter+'_'+fromplatform+'_'+fromcomponent+'/'
                
                createDir(directory)

                LocationPolicy=directory+'TO_'+tocenter+'_'+toplatform+'_'+tocomponent+'/'

                createDir(LocationPolicy)

                PolicyName = 'S3PDGS_DC_Policy_'+policy_id+'.From_'+fromcenter+'_'+fromplatform+'_'+fromcomponent+'.TO_'+tocenter+'_'+toplatform+'_'+tocomponent      +'.'+datatype+'.Version-'+policyversion+'.xml'
                
                st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')            
                
                if 'partial' in suffixprefix:
                    with open(LocationPolicy+PolicyName,"w") as f:
                        f.write('<?xml version="1.0" encoding="UTF-8"?>\r\n')
                        f.write('<!-- Sentinel-3 PDGS Marine centre (EUMETSAT) -->\r\n')
                        f.write('<!-- Circulation Policy Generated on date: '+st+'-->\r\n')
                        f.write('<CirculationPolicyConfigurationRequest>\r\n')
                        f.write('\t<InstallationNode>'+installationnode+'</InstallationNode>\r\n')
                        f.write('\t<ActionType>INSERT</ActionType>\r\n')
                        f.write('\t<!--     >1234567890123456< max 16 chars for DataType-->\r\n')
                        f.write('\t<DataType>'+datatype+'</DataType>\r\n')
                        f.write('\t<DataRegExp>'+regex+'</DataRegExp>\r\n')
                        f.write('\t<DataProvider>\r\n')
                        f.write('\t\t<TransferMethod>'+src_protocol+'</TransferMethod>\r\n')
                        f.write('\t\t<Host>'+src_host+'</Host>\r\n')
                        f.write('\t\t<Path>'+src_path+'</Path>\r\n')
                        f.write('\t\t<User>'+src_user+'</User>\r\n')
                        f.write('\t\t<Password>'+src_password+'</Password>\r\n')
                        f.write('\t</DataProvider>\r\n')
                        f.write('\t<DataConsumer>\r\n')
                        f.write('\t\t<TransferMethod>'+dest_protocol+'</TransferMethod>\r\n')
                        f.write('\t\t<Host>'+dest_host+'</Host>\r\n')
                        f.write('\t\t<Path>'+dest_path+'</Path>\r\n')
                        f.write('\t\t<User>'+dest_user+'</User>\r\n')
                        f.write('\t\t\<Password>'+dest_password+'</Password>\r\n')
                        f.write('\t<TmpFilename>suffix</TmpFilename>\r\n')
                        f.write('\t<TmpFilenameValue>.partial</TmpFilenameValue>\r\n')
                        f.write('\t</DataConsumer>\r\n')
                        f.write('\t<Priority>10</Priority>\r\n')
                        f.write('</CirculationPolicyConfigurationRequest>\r\n')
                        f.close()
                else:
                    try:
                        with open(LocationPolicy+PolicyName,"w+") as f:
                            f.write('<?xml version="1.0" encoding="UTF-8"?>\r\n')
                            f.write('<!-- Sentinel-3 PDGS Marine centre (EUMETSAT) -->\r\n')
                            f.write('<!-- Circulation Policy Generated on date: '+st+'-->\r\n')
                            f.write('<CirculationPolicyConfigurationRequest>\r\n')
                            f.write('\t<InstallationNode>'+installationnode+'</InstallationNode>\r\n')
                            f.write('\t<ActionType>INSERT</ActionType>\r\n')
                            f.write('\t<!--     >1234567890123456< max 16 chars for DataType-->\r\n')
                            f.write('\t<DataType>'+datatype+'</DataType>\r\n')
                            f.write('\t<DataRegExp>'+regex+'</DataRegExp>\r\n')
                            f.write('\t<DataProvider>\r\n')
                            f.write('\t\t<TransferMethod>'+src_protocol+'</TransferMethod>\r\n')
                            f.write('\t\t<Host>'+src_host+'</Host>\r\n')
                            f.write('\t\t<Path>'+src_path+'</Path>\r\n')
                            f.write('\t\t<User>'+src_user+'</User>\r\n')
                            f.write('\t\t<Password>'+src_password+'</Password>\r\n')
                            f.write('\t</DataProvider>\r\n')
                            f.write('\t<DataConsumer>\r\n')
                            f.write('\t\t<TransferMethod>'+dest_protocol+'</TransferMethod>\r\n')
                            f.write('\t\t<Host>'+dest_host+'</Host>\r\n')
                            f.write('\t\t<Path>'+dest_path+'</Path>\r\n')
                            f.write('\t\t<User>'+dest_user+'</User>\r\n')
                            f.write('\t\t<Password>'+dest_password+'</Password>\r\n')
                            f.write('\t</DataConsumer>\r\n')
                            f.write('\t<Priority>10</Priority>\r\n')
                            f.write('</CirculationPolicyConfigurationRequest>\r\n')
                            f.close()
                    except IOError as (errno,strerror):
                        print "I/O error({0}): {1}".format(errno, strerror)
               
            count = count +1
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))




