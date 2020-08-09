# 14. nodarbība - Web service and ngrok

Šajā nodarbībā es pameģināju palaist savu SimpleHTTP serveri. Lai to izdarītu, es ievadīju komandrindā sekojošu komandu:

	python -m SimpleHTTPServer 8000

Kad serveris tiek palaists, mēs varam redzēt aktuālā direktorija saturu. Piemēram, ja es palaižu serveri direktorijā P12_HTML_and_CSS, tad es redzēšu direktorijas saturu:

![Direktorija saturs](https://github.com/daniil172101/RTR108/blob/master/darbi/P14_web_service/web_service_1.png) 

Es arī atvēru savu HTML failu *voltage_divider.html*, lai paradīt, kā izskatās fails: 

![HTML faila saturs](https://github.com/daniil172101/RTR108/blob/master/darbi/P14_web_service/web_service_2.png)

Bet šis serveris ir pieejams tikai lokāli.Lai viņš būtu pieejams globāli, es izmantoju tunelēšanas rīku ngrok. Rezultāts ir redzams šeit:

![Globāli pieejams HTML fails](https://github.com/daniil172101/RTR108/blob/master/darbi/P14_web_service/web_service_3.png)

Arī es pārbaudīju, vai serveris ir pieejams uz cita datora:

![Faila pieejamība uz cita datora](https://github.com/daniil172101/RTR108/blob/master/darbi/P14_web_service/web_service_4.png)

