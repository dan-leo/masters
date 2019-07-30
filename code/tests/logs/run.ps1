# pytest -svk echo C:\GIT\masters\code\tests | tee-object -append -filepath ./tdump
# powershell.exe -noprofile -command { $path\test_main.ps1 | tee-object $log }
# powershell.exe -noprofile -command { pytest -svk echo C:\GIT\masters\code\tests | tee-object -append -filepath ./terminaldump }