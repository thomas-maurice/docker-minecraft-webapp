#!/usr/bin/env python

import subprocess

if __name__ == "__main__":
    process = subprocess.Popen(
            ["/usr/bin/java", "-Xms1024M", "-Xmx4G", "-jar", "./server.jar"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            close_fds=True,
            cwd="/minecraft"
    )
