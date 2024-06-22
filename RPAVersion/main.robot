*** Settings ***
Library    ImageHorizonLibrary    reference_folder=${CURDIR}${/}screenshotsElementos    confidence=0.7
Library    OperatingSystem
Library    Process
Library    String

*** Variables ***
${USERNAME}    nicezefer@gmail.com
${PASSWORD}    
${CHROME_PATH}    C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe
${URL}     https://www.infojobs.net/candidate/candidate-login/candidate-login.xhtml?dgv=1718954201266

*** Keywords ***
#Esto vendría a ser la declaración de funciones
Navigate URL
    [Arguments]         ${URL}     ${searchBarScr}
    Wait For      ${searchBarScr}    timeout=5
    Click Image   ${searchBarScr} 
    Type          ${URL}   
    Type          Key.Enter

Manipular Cookies
    [Arguments]    ${decision}    ${cookiesWindowScr}
    Wait For    ${cookiesWindowScr}    timeout=5
    Run Keyword If    '${decision}' == '${True}'
    ...    Click Image    aceptarcookies
    ...    ELSE
    ...    Click Image    rechazarcookies
    
Login
   [Arguments]    ${username}    ${password}
   Click Image    fieldemail
   ${usernameSplit}=    Split String   ${username}    @
   Type    ${usernameSplit}[0]
   Type With Keys Down    2    Key.altright
   Type    ${usernameSplit}[1]
   Press Combination    Key.Tab
   Type    ${password}
   Press Combination    Key.Enter
   


*** Test Cases ***
#Aquí van todos los pasos a realizar, separar cada uno permite hacer un mejor seguimiento
Abrir Browser y navegar a URL
    Start Process    ${CHROMEPATH}    --incognito    --start-maximized
    Sleep    2
    Set Confidence    0.7
    Navigate URL    ${URL}     searchbar
#El siguiente sleep lo coloco para darle tiempo a la ventana de cookies en aparecer
    Sleep    3

Manipular ventana de cookies
    Set Confidence    0.5
    Manipular Cookies    True    windowcookies
   
Hacer Login
    Login    ${USERNAME}    ${PASSWORD}
    Sleep    2
    
Ir a Mis Ofertas
    Wait For    misofertasbtn    5
    Click Image    misofertasbtn
