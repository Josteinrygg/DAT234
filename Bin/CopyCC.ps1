Write-Host "Caesar Cipher"

$EType = read-host "Enter 'YES' if you want to start the Decryption of the nonsense"
[int]$key = read-host "Enter the key to the kingdom"
$msg = read-host "Give me the nonsense"
Write-Host "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" 
  
#Decrypt
if ($EType -eq "YES")
{

Write-Host "Encrypted: " $msg -foregroundcolor "red"

$String=[char[]]$msg

Write-Host "Answer Letter ASCII Values" -foregroundcolor "red" #Hide

foreach ($letter in $String) #Hide (the foreeach cmd)
{
    $nbr = [int[]][char]$letter
    Write-Host $nbr -foregroundcolor "red"
}

Write-Host "Answer Letter ASCII Values"  -foregroundcolor "blue" #Hide

$String=[char[]]$msg
foreach ($letter in $String)
{
    $nbr = [int[]][char]$letter
   
    If ($nbr -ge 0 -and $nbr -le 64) #ASCII Codes
       {
       [string]$Snbr = $nbr
       [int]$Nnbr = $Snbr  
       [int]$Enbr = $Nnbr 
       Write-Host $Enbr -foregroundcolor "blue"#Hide
       [string]$ELetter = [char]$Enbr
       }
  
    If ($nbr -ge 65 -and $nbr -le 90) #Alphabet UpperCase
       {
       [string]$Snbr = $nbr
       [int]$Nnbr = $Snbr 
       [int]$nkey = $key
       [int]$Enbr = $Nnbr - $nkey 
       If ($Enbr -gt 90) {$Enbr = $Enbr - 26}
       If ($Enbr -lt 65) {$Enbr = $Enbr + 26}
       Write-Host $Enbr -foregroundcolor "blue" #Hide
       [string]$ELetter = [char]$Enbr
       #Write-Host "Lowercase " + $ELetter        
       }  
   
    If ($nbr -ge 91 -and $nbr -le 96) #ASCII Codes
       {
       [string]$Snbr = $nbr
       [int]$Nnbr = $Snbr  
       [int]$Enbr = $Nnbr 
       Write-Host $Enbr -foregroundcolor "blue"
       [string]$ELetter = [char]$Enbr
       }
          
    If ($nbr -ge 97 -and $nbr -le 122) #Alphabet LowerCase
       {
       [string]$Snbr = $nbr
       [int]$Nnbr = $Snbr 
       [int]$nkey = $key
       [int]$Enbr = $Nnbr - $nkey 
       If($Enbr -gt 122) {$Enbr = $Enbr - 26}
       If  ($Enbr -lt 97) {$Enbr = $Enbr + 26}
       Write-Host $Enbr -foregroundcolor "blue" #Hide
       [string]$ELetter = [char]$Enbr       
       }    
     
    If ($nbr -ge 123 -and $nbr -le 127) #ASCII Codes
       {
       [string]$Snbr = $nbr
       [int]$Nnbr = $Snbr  
       [int]$Enbr = $Nnbr 
       Write-Host $Enbr -foregroundcolor "blue" #Hide
       [string]$ELetter = [char]$Enbr
       }    

$EMsg = $EMsg + $ELetter    
} 
Write-Host "Answer: " $EMsg -foregroundcolor "blue"
Clear-variable EMsg
Write-Host "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
}