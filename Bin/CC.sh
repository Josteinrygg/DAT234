#!/usr/bin/env bash
$Text ="CbjrefuryyVfNjrfbzr"
echo $Text
$Bytes = [System.Text.Endcoding]::Unicode.GetBytes($Text)

$Encoded = [Convert]::ToBase64String($Bytes)
echo $Encoded

$Decoded =[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($Encoded))
echo $D
