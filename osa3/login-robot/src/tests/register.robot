*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalikkaa    kaliiopopopopopo9
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalikka    kali7899997890989
    Output Should Contain  User with username kalikka already exists

Register With Too Short Username And Valid Password
    Input Credentials  k    kali78999934567
    Output Should Contain  Virheellinen

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kali67    kali789999jhjl
    Output Should Contain  Virheellinen

Register With Valid Username And Too Short Password
    Input Credentials  kalikointi    kalik
    Output Should Contain  Virheellinen

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalikointki    kalikkamaa
    Output Should Contain  Virheellinen

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalikka  kalikointilaitos67