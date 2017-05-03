@REM 
@REM Run AnyLogic Experiment
@REM 
@CHCP 1252>nul 
@SET DIR_BACKUP_XJAL=%CD%
@CD /D "%~dp0"
@SET DISK_XJAL=C:
@IF NOT [%SystemDrive%]==[] SET DISK_XJAL=%SystemDrive%
@SET PATH_XJAL="%DISK_XJAL%\Program Files\Java\jre8\bin\java.exe"
@IF NOT EXIST %PATH_XJAL% SET PATH_XJAL="%ProgramFiles%\Java\jre8\bin\java.exe"
@IF NOT EXIST %PATH_XJAL% SET PATH_XJAL="%DISK_XJAL%\Program Files (x86)\Java\jre8\bin\java.exe"
@IF NOT EXIST %PATH_XJAL% SET PATH_XJAL="%ProgramFiles(x86)%\Java\jre8\bin\java.exe"
@IF NOT EXIST %PATH_XJAL% SET PATH_XJAL="%JAVA_HOME%\bin\java.exe"
@IF NOT EXIST %PATH_XJAL% SET PATH_XJAL=java
%PATH_XJAL% -Djava.security.policy=security.policy sun.applet.AppletViewer "SH2O_D73_SES_obs2.html"
@CD /D "%DIR_BACKUP_XJAL%"
