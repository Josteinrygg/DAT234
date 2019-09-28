function decrypt(){
    $input  = Read-host "Input what you want to decrypt"
    $key = Read-host "Give me the key"
    $rows = $input.Length/$key
    $decrypted = ""
    
    
    for($i=0;$i -lt $rows; $i++){
    for ($o=0; $o -lt $key; $o++){
    $decrypted += $input[$i+$o*$rows]
    }#end for
    }#end for 
    echo $decrypted
    }#end decrypt 
    
    function encrypt(){
    $input  = Read-host "Input what you want to ecrypt"
    $key = Read-host "Give me the key"
    $rows = $input.Length/$key
    $encrypted = ""
    
    for ($i=0; $i -lt $key;$i++){
    for ($o=0; $o -lt $rows; $o++){
    $encrypted += $input[$i + $o *$key]
    }#for end
    }#for end
    echo $encrypted
    }#end encrypt 