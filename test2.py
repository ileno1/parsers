import re 
import pandas as pd 

ex = """<SUBBEGIN
	SUBID=+541160798354;
	PbxUserFlag=0;
	CONSFLG=0;
	HssIndex=0;
	<IMPIBEGIN
		IMPI=+541160798354@ims.mnc007.mcc722.3gppnetwork.org;
		CHRGTPLID=27;
		AuthenticationType=SDA;
	<IMPIEND
	<IMPUBEGIN
		IMPU=sip:+541160798354@ims.mnc007.mcc722.3gppnetwork.org;
		IMPI=+541160798354@ims.mnc007.mcc722.3gppnetwork.org;
		Shared=0;
		VNCFlag=1;
		IMSRoamID=10;
		BarringIndication=0;
		IRSID=1;
		DefaultIMPU=0;
		AuthRegFlag=1;
		NNCFlag=0;
		NASSRoamID=255;
		UserPriority=2;
		LooseRouteIndication=0;
		UserState=1;
		CurSCSCFName=sip:scscfvlz.ims.mnc007.mcc722.3gppnetwork.org:5060;
		StdPriority=255;
		<REFLOCINFOBEGIN
			RefLocIndex=1;
			RefLocInfo=line-id=+541160798354;cc=722;oc=07;lac=444;ali=0;
			RefLocType=12;
			DefaultRLI=1;
		<REFLOCINFOEND
		IMPUType=1;
		CONSFLG_PU=0;
	<IMPUEND
	<IMPUBEGIN
		IMPU=tel:+541160798354;
		IMPI=+541160798354@ims.mnc007.mcc722.3gppnetwork.org;
		Shared=0;
		VNCFlag=1;
		IMSRoamID=10;
		BarringIndication=0;
		IRSID=1;
		DefaultIMPU=0;
		AuthRegFlag=1;
		NNCFlag=0;
		NASSRoamID=255;
		UserPriority=2;
		LooseRouteIndication=0;
		UserState=1;
		CurSCSCFName=sip:scscfvlz.ims.mnc007.mcc722.3gppnetwork.org:5060;
		StdPriority=255;
		<REFLOCINFOBEGIN
			RefLocIndex=1;
			RefLocInfo=line-id=+541160798354;cc=722;oc=07;lac=444;ali=0;
			RefLocType=12;
			DefaultRLI=1;
		<REFLOCINFOEND
		IMPUType=1;
		CONSFLG_PU=0;
	<IMPUEND
	<IMPUBEGIN
		IMPU=sip:+541160798354@voip.ims.mnc007.mcc722.3gppnetwork.org;
		IMPI=+541160798354@ims.mnc007.mcc722.3gppnetwork.org;
		Shared=0;
		VNCFlag=1;
		IMSRoamID=10;
		BarringIndication=0;
		IRSID=1;
		DefaultIMPU=1;
		AuthRegFlag=1;
		NNCFlag=0;
		NASSRoamID=255;
		UserPriority=2;
		LooseRouteIndication=0;
		UserState=1;
		CurSCSCFName=sip:scscfvlz.ims.mnc007.mcc722.3gppnetwork.org:5060;
		StdPriority=255;
		<REFLOCINFOBEGIN
			RefLocIndex=1;
			RefLocInfo=line-id=+541160798354;cc=722;oc=07;lac=444;ali=0;
			RefLocType=12;
			DefaultRLI=1;
		<REFLOCINFOEND
		IMPUType=1;
		<REPOSITDATABEGIN
			ServiceIndication=MmtServiceConfig;
			SequenceNumber=6;
			ServiceData=
        <mmt-data:telephony-service-configuration version="3.1" xmlns="http://uri.etsi.org/ngn/params/xml/simservs/xcap" xmlns:cp="urn:ietf:params:xml:ns:common-policy" xmlns:mmt-data="http://schemas.ericsson.com/mmtel/service-data" xmlns:mmt-op="http://schemas.ericsson.com/mmtel/operator-service-data" xmlns:mmt-serv="http://schemas.ericsson.com/mmtel/services" xmlns:ocp="urn:oma:xml:xdm:common-policy" xmlns:ss="http://uri.etsi.org/ngn/params/xml/simservs/xcap">
            <mmt-data:user-configuration>
                <ss:simservs><ss:communication-diversion active="true"><cp:ruleset/></ss:communication-diversion><ss:originating-identity-presentation-restriction active="false"><ss:default-behaviour>presentation-not-restricted</ss:default-behaviour></ss:originating-identity-presentation-restriction><mmt-serv:outgoing-barring-programs active="true"><mmt-serv:single-program>15</mmt-serv:single-program></mmt-serv:outgoing-barring-programs></ss:simservs>
            </mmt-data:user-configuration>
            <mmt-data:operator-configuration>
                <mmt-data:operator-service-data><mmt-op:operator-calling-party-category activated="true"><mmt-op:cpc-value>ordinary</mmt-op:cpc-value></mmt-op:operator-calling-party-category><mmt-op:operator-communication-diversion activated="true"><mmt-op:conditions><mmt-op:unconditional activated="false"/></mmt-op:conditions></mmt-op:operator-communication-diversion><mmt-op:operator-media-policy activated="true"><cp:ruleset><cp:rule id="video"><cp:conditions><ss:media>video</ss:media></cp:conditions><cp:actions><ss:allow>false</ss:allow></cp:actions></cp:rule></cp:ruleset></mmt-op:operator-media-policy><mmt-op:operator-originating-identity-presentation-restriction activated="true"><mmt-op:mode>temporary</mmt-op:mode><mmt-op:restriction>all-private-information</mmt-op:restriction></mmt-op:operator-originating-identity-presentation-restriction><mmt-op:operator-supplementary-service-codes activated="true"/><mmt-op:operator-user-call-admission-control activated="true"><mmt-op:orig-active-limit>1</mmt-op:orig-active-limit><mmt-op:term-active-limit>1</mmt-op:term-active-limit><mmt-op:total-active-limit>1</mmt-op:total-active-limit><mmt-op:orig-all-limit>2</mmt-op:orig-all-limit><mmt-op:term-all-limit>2</mmt-op:term-all-limit><mmt-op:total-all-limit>2</mmt-op:total-all-limit><mmt-op:waiting-limit>0</mmt-op:waiting-limit></mmt-op:operator-user-call-admission-control><mmt-op:operator-outgoing-barring-programs activated="true"><mmt-op:scheme>single</mmt-op:scheme></mmt-op:operator-outgoing-barring-programs><mmt-op:operator-carrier-pre-select activated="true"><mmt-op:call-type-carrier call-type="CPS-National"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier><mmt-op:call-type-carrier call-type="CPS-International"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier><mmt-op:call-type-carrier call-type="CPS-Mobile"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier><mmt-op:call-type-carrier call-type="Local"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier></mmt-op:operator-carrier-pre-select></mmt-data:operator-service-data>
            <mmt-op:operator-common-data><mmt-op:area-code>11</mmt-op:area-code><mmt-op:country-code>54</mmt-op:country-code></mmt-op:operator-common-data></mmt-data:operator-configuration>
        </mmt-data:telephony-service-configuration>
    ;
		<REPOSITDATAEND
		CONSFLG_PU=0;
	<IMPUEND
	<SPINFBEGIN
		IMPU=sip:+541160798354@ims.mnc007.mcc722.3gppnetwork.org;
		IMPU=tel:+541160798354;
		IMPU=sip:+541160798354@voip.ims.mnc007.mcc722.3gppnetwork.org;
		MediaProfileID=4294967295;
		<IFCINFBEGIN
			Priority=100;
			ProfilePartIndicator=1;
			ASAddress=sip:mmteltermunreg.ims.mnc007.mcc722.3gppnetwork.org;call=term_unregistered;lr;
			DefaultHandling=0;
			ServiceInformation=MMTel-AS;
			TriggerPoint=<TriggerPoint><ConditionTypeCNF>0</ConditionTypeCNF><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><SessionCase>2</SessionCase></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><Method>INVITE</Method></SPT></TriggerPoint>;
			IncludeRegReq=0;
			InclueRegRsp=0;
		<IFCINFEND
		SharediFCSetID=27;
		SharediFCSetID_1=-1;
		SharediFCSetID_2=-1;
		SharediFCSetID_3=-1;
	<SPINFEND
<SUBEND
<SUBBEGIN
	SUBID=+541122057966;
	PbxUserFlag=0;
	CONSFLG=0;
	HssIndex=0;
	<IMPIBEGIN
		IMPI=+541122057966@ims.mnc007.mcc722.3gppnetwork.org;
		CHRGTPLID=27;
		AuthenticationType=SDA;
	<IMPIEND
	<IMPUBEGIN
		IMPU=tel:+541122057966;
		IMPI=+541122057966@ims.mnc007.mcc722.3gppnetwork.org;
		Shared=0;
		VNCFlag=1;
		IMSRoamID=10;
		BarringIndication=0;
		IRSID=1;
		DefaultIMPU=0;
		AuthRegFlag=1;
		NNCFlag=0;
		NASSRoamID=255;
		UserPriority=2;
		LooseRouteIndication=0;
		CurSCSCFName=sip:scscfvlz.ims.mnc007.mcc722.3gppnetwork.org:5060;
		StdPriority=255;
		<REFLOCINFOBEGIN
			RefLocIndex=1;
			RefLocInfo=line-id=+541122057966;cc=722;oc=07;lac=671;ali=0;
			RefLocType=12;
			DefaultRLI=1;
		<REFLOCINFOEND
		IMPUType=1;
		CONSFLG_PU=0;
	<IMPUEND
	<IMPUBEGIN
		IMPU=sip:+541122057966@ims.mnc007.mcc722.3gppnetwork.org;
		IMPI=+541122057966@ims.mnc007.mcc722.3gppnetwork.org;
		Shared=0;
		VNCFlag=1;
		IMSRoamID=10;
		BarringIndication=0;
		IRSID=1;
		DefaultIMPU=0;
		AuthRegFlag=1;
		NNCFlag=0;
		NASSRoamID=255;
		UserPriority=2;
		LooseRouteIndication=0;
		CurSCSCFName=sip:scscfvlz.ims.mnc007.mcc722.3gppnetwork.org:5060;
		StdPriority=255;
		<REFLOCINFOBEGIN
			RefLocIndex=1;
			RefLocInfo=line-id=+541122057966;cc=722;oc=07;lac=671;ali=0;
			RefLocType=12;
			DefaultRLI=1;
		<REFLOCINFOEND
		IMPUType=1;
		CONSFLG_PU=0;
	<IMPUEND
	<IMPUBEGIN
		IMPU=sip:+541122057966@voip.ims.mnc007.mcc722.3gppnetwork.org;
		IMPI=+541122057966@ims.mnc007.mcc722.3gppnetwork.org;
		Shared=0;
		VNCFlag=1;
		IMSRoamID=10;
		BarringIndication=0;
		IRSID=1;
		DefaultIMPU=1;
		AuthRegFlag=1;
		NNCFlag=0;
		NASSRoamID=255;
		UserPriority=2;
		LooseRouteIndication=0;
		CurSCSCFName=sip:scscfvlz.ims.mnc007.mcc722.3gppnetwork.org:5060;
		StdPriority=255;
		<REFLOCINFOBEGIN
			RefLocIndex=1;
			RefLocInfo=line-id=+541122057966;cc=722;oc=07;lac=671;ali=0;
			RefLocType=12;
			DefaultRLI=1;
		<REFLOCINFOEND
		IMPUType=1;
		<REPOSITDATABEGIN
			ServiceIndication=MmtServiceConfig;
			SequenceNumber=7;
			ServiceData=
        <mmt-data:telephony-service-configuration version="3.1" xmlns="http://uri.etsi.org/ngn/params/xml/simservs/xcap" xmlns:cp="urn:ietf:params:xml:ns:common-policy" xmlns:mmt-data="http://schemas.ericsson.com/mmtel/service-data" xmlns:mmt-op="http://schemas.ericsson.com/mmtel/operator-service-data" xmlns:mmt-serv="http://schemas.ericsson.com/mmtel/services" xmlns:ocp="urn:oma:xml:xdm:common-policy" xmlns:ss="http://uri.etsi.org/ngn/params/xml/simservs/xcap">
            <mmt-data:user-configuration>
                <ss:simservs><ss:communication-diversion active="true"/><mmt-serv:outgoing-barring-programs active="true"><mmt-serv:single-program>0</mmt-serv:single-program></mmt-serv:outgoing-barring-programs><ss:originating-identity-presentation-restriction active="false"><ss:default-behaviour>presentation-not-restricted</ss:default-behaviour></ss:originating-identity-presentation-restriction></ss:simservs>
            </mmt-data:user-configuration>
            <mmt-data:operator-configuration>
                <mmt-data:operator-service-data><mmt-op:operator-calling-party-category activated="true"><mmt-op:cpc-value>ordinary</mmt-op:cpc-value></mmt-op:operator-calling-party-category><mmt-op:operator-carrier-pre-select activated="true"><mmt-op:call-type-carrier call-type="CPS-National"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier><mmt-op:call-type-carrier call-type="CPS-International"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier><mmt-op:call-type-carrier call-type="CPS-Mobile"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier><mmt-op:call-type-carrier call-type="Local"><mmt-op:carrier-code>+54222</mmt-op:carrier-code></mmt-op:call-type-carrier></mmt-op:operator-carrier-pre-select><mmt-op:operator-communication-diversion activated="true"><mmt-op:conditions><mmt-op:unconditional activated="false"/></mmt-op:conditions></mmt-op:operator-communication-diversion><mmt-op:operator-media-policy activated="true"><cp:ruleset><cp:rule id="video"><cp:conditions><ss:media>video</ss:media></cp:conditions><cp:actions><ss:allow>false</ss:allow></cp:actions></cp:rule></cp:ruleset></mmt-op:operator-media-policy><mmt-op:operator-outgoing-barring-programs activated="true"><mmt-op:scheme>single</mmt-op:scheme></mmt-op:operator-outgoing-barring-programs><mmt-op:operator-originating-identity-presentation-restriction activated="true"><mmt-op:mode>temporary</mmt-op:mode><mmt-op:restriction>all-private-information</mmt-op:restriction></mmt-op:operator-originating-identity-presentation-restriction><mmt-op:operator-supplementary-service-codes activated="true"/><mmt-op:operator-user-call-admission-control activated="true"><mmt-op:orig-active-limit>1</mmt-op:orig-active-limit><mmt-op:term-active-limit>1</mmt-op:term-active-limit><mmt-op:total-active-limit>1</mmt-op:total-active-limit><mmt-op:orig-all-limit>2</mmt-op:orig-all-limit><mmt-op:term-all-limit>2</mmt-op:term-all-limit><mmt-op:total-all-limit>2</mmt-op:total-all-limit><mmt-op:waiting-limit>0</mmt-op:waiting-limit></mmt-op:operator-user-call-admission-control><mmt-op:operator-voice-mail activated="true"><mmt-op:voice-mail-address>sip:+541131@voip.ims.mnc007.mcc722.3gppnetwork.org;user=phone</mmt-op:voice-mail-address></mmt-op:operator-voice-mail></mmt-data:operator-service-data>
            <mmt-op:operator-common-data><mmt-op:area-code>11</mmt-op:area-code><mmt-op:country-code>54</mmt-op:country-code></mmt-op:operator-common-data></mmt-data:operator-configuration>
        </mmt-data:telephony-service-configuration>
    ;
		<REPOSITDATAEND
		CONSFLG_PU=0;
	<IMPUEND
	<SPINFBEGIN
		IMPU=tel:+541122057966;
		IMPU=sip:+541122057966@ims.mnc007.mcc722.3gppnetwork.org;
		IMPU=sip:+541122057966@voip.ims.mnc007.mcc722.3gppnetwork.org;
		MediaProfileID=4294967295;
		<IFCINFBEGIN
			Priority=100;
			ProfilePartIndicator=1;
			ASAddress=sip:mmteltermunreg.ims.mnc007.mcc722.3gppnetwork.org;call=term_unregistered;lr;
			DefaultHandling=0;
			ServiceInformation=MMTel-AS;
			TriggerPoint=<TriggerPoint><ConditionTypeCNF>0</ConditionTypeCNF><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><SessionCase>2</SessionCase></SPT><SPT><ConditionNegated>0</ConditionNegated><Group>0</Group><Method>INVITE</Method></SPT></TriggerPoint>;
			IncludeRegReq=0;
			InclueRegRsp=0;
		<IFCINFEND
		SharediFCSetID=27;
		SharediFCSetID_1=-1;
		SharediFCSetID_2=-1;
		SharediFCSetID_3=-1;
	<SPINFEND
<SUBEND"""

import re
import pandas as pd
s = open('E:\\Downloads\\MemExpFile_HSS9860_31.txt', 'r')
s = s.readlines()
s = str(s[1:])

# Regex matches one IMPI with next UserState - any IMPI in between is skipped
regex =  r"IMPI=(?P<IMPI>)[+0-9]+[^\d][a-z]+[^\d][a-z]+[0-9]+[^\d][a-z]+[0-9]+[^\d][3][a-z]+[^\d][a-z]+"
regex2 = r"UserState=(?P<UserState>[1-2]+)"
regex3 = r'[^\d](SUBBEGIN)'
regex4 = r'[^\d](SUBEND)'
data_dict = {}
def parse_data(s):
	data = []
	if re.search(regex3, s):
		for match in re.finditer(regex, s):
			if match.group():
				if re.search(regex4, s):
					matches1 = match.group()
					list_impu = matches1.split('=')
					data.append(list_impu)
		for match in re.finditer(regex2, s):
			if match.group():
				if re.search(regex4,s):
					matches2 = match.group()
					list_user = matches2.split('=')
					data.append(list_user)
				else:
					if match.group() is None:
						empty = 'UserState=0'
						list_empty = empty.split('=')
						data.append(list_empty)
	return data

for i in parse_data(s):
    if i[0] not in data_dict:
        data_dict[i[0]] = [i[1]]

    else:
        data_dict[i[0]].append(i[1])

pd.DataFrame.from_dict(data_dict, orient = 'index').T.to_csv('filename2.csv')
