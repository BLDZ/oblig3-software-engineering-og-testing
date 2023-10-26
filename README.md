# oblig3-software-engineering-og-testing
 Oblig 3 i faget Software Engineering og Testing

Jeg begynte oppgaven med å lage et GitHub repository med python filene ifra oblig 2. Jeg lastet så dette lokale repository opp til GitHub.

Jeg prøvde så å lese meg opp på hvordan jeg skulle løse denne oppgaven. Det første som jeg forsøkte meg på var å bruke en ferdiglagd workflow som het "Python application". Jeg lagde en branch hvor jeg testet meg med den. Jeg prøvde meg litt frem med den men fikk den ikke til å fungere som jeg ville. Jeg fikk også intrykk om at den var ment til større prosjekt så jeg bestemte meg heller for å finne en annen løsning.

Den andre løsningen fant jeg etter å ha lest meg opp litt mer på hvordan GitHub actions og workflows fungerte. Jeg bestemte meg for å lage min egen workflow. Jeg baserte den på et eksempel jeg fant her: https://blog.devgenius.io/automating-your-python-unit-tests-with-github-actions-a-step-by-step-guide-26d1ed7c07a8 . Jeg modifiserte den slik at den skulle fungere til mitt bruk.

Etter litt troubleshooting som kom ifra at jeg hadde skrevet ubuntu feil i yml filen så fikk jeg det til å fungere. Jeg lagde en branch til så jeg kunne endre på python filene for å sjekke om testene faktisk runnet riktig, og det gjorde de.

English:

I started the task by creating a GitHub repository with the python files from oblig 2. I then uploaded this local repository to GitHub.

Then I tried to read up on how to solve the task. The first thing I tried was to use a ready-made workflow called "Python application". I made a branch where I tested it for myself. I tried but couldn't get it to work as I wanted. I also got the impression that it was intended for a larger project, so I decided to find another solution.

I found the second solution after reading up a bit more on how GitHub actions and workflows worked. I decided to create my own workflow. I based it on an example I found here: https://blog.devgenius.io/automating-your-python-unit-tests-with-github-actions-a-step-by-step-guide-26d1ed7c07a8 . I modified it to work for my use.

After some troubleshooting which came from the fact that I had written ubuntu incorrectly in the yml file, I got it to work. I made another branch so I could change the python files to check if the tests actually ran correctly, and they did.
