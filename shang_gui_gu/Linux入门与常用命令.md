# Linux 入门与常用命令（Ubuntu）

本文面向 Linux 初学者和一般开发者，以 **Ubuntu** 为主要操作环境。阅读后，你应当能够理解 Linux 的基本工作原理，熟悉目录、文件、权限、进程、软件包、网络和服务管理，并能够在终端中完成日常开发操作。

> 文中的命令主要适用于 Ubuntu 22.04 LTS、Ubuntu 24.04 LTS 及相近版本。不同 Ubuntu 版本之间可能存在少量差异。

## 1. Linux、GNU 与 Ubuntu 是什么

### 1.1 Linux 严格来说是内核

Linux 最初由 Linus Torvalds 于 1991 年发布。严格来说，Linux 指的是操作系统的**内核（Kernel）**，它负责：

- 管理 CPU、内存、磁盘、网卡等硬件；
- 创建、调度和结束进程；
- 管理文件系统；
- 提供用户、权限和安全机制；
- 为应用程序提供系统调用接口。

用户平时使用的完整 Linux 系统，通常还包括 GNU 工具、Shell、软件包管理器、桌面环境和各种应用程序。因此，也常称为 GNU/Linux。

### 1.2 什么是 Linux 发行版

发行版（Distribution，常缩写为 **distro**）是将 Linux 内核和一整套软件组合、测试、发布出来的完整操作系统。常见发行版包括：

- Ubuntu：基于 Debian，易用、资料丰富，适合桌面、开发和服务器；
- Debian：稳定，软件自由度高，很多发行版以它为基础；
- Red Hat Enterprise Linux（RHEL）：面向企业；
- Rocky Linux、AlmaLinux：兼容 RHEL 的社区发行版；
- Fedora：技术更新较快；
- Arch Linux：高度可定制，适合有经验的用户。

本文使用的 **Ubuntu** 就是一种 Linux 发行版。Ubuntu 中默认使用 `apt` 管理软件，软件包底层格式为 `.deb`。

### 1.3 Linux 系统的层次

可以把 Linux 的工作过程简化为：

```text
用户
  ↓ 输入命令
终端与 Shell（例如 Bash）
  ↓ 启动程序、请求系统服务
应用程序与系统工具
  ↓ 系统调用
Linux 内核
  ↓ 驱动硬件
CPU、内存、磁盘、网卡等硬件
```

- **终端（Terminal）**：输入和显示文本的窗口；
- **Shell**：解释命令的程序，例如 Bash、Zsh；
- **Bash**：Ubuntu 中常见的 Shell，名称来自 **Bourne Again Shell**；
- **内核（Kernel）**：直接管理系统资源；
- **命令**：Shell 内建功能或磁盘上的可执行程序。

终端不等于 Shell。终端更像一个交互窗口，Shell 才是真正读取并解释命令的程序。

## 2. Linux 的核心思想

### 2.1 一切皆文件

Linux 尽量通过统一的“文件”接口表示不同资源：

- 普通文件是文件；
- 目录是一种特殊文件；
- 磁盘设备可表示为 `/dev/sda`；
- 终端可表示为 `/dev/tty`；
- 进程和内核信息可通过 `/proc` 中的虚拟文件查看。

这并不表示所有对象真的存放在磁盘中，而是说很多资源可以使用类似文件的方式读取和操作。

### 2.2 小工具组合完成复杂任务

很多 Linux 命令只专注一件事，然后通过管道 `|` 组合：

```bash
ps aux | grep python
```

这条命令先由 `ps` 输出进程，再由 `grep` 筛选包含 `python` 的行。

### 2.3 多用户与权限隔离

Linux 从设计上支持多个用户同时工作。每个文件和进程都有所属用户，普通用户默认不能随意修改系统文件。需要临时使用管理员权限时，Ubuntu 通常使用 `sudo`。

### 2.4 区分大小写

Linux 文件名和命令通常区分大小写：

```text
README.md
readme.md
```

它们是两个不同的文件。`cd` 和 `CD` 也不是同一个命令。

## 3. 认识终端和命令格式

终端提示符可能类似：

```text
alice@ubuntu:~/project$
```

- `alice`：当前用户名；
- `ubuntu`：主机名；
- `~/project`：当前目录；
- `$`：普通用户提示符；
- `#`：通常表示 root 用户提示符。

命令的一般结构如下：

```text
命令 [选项] [参数]
```

例如：

```bash
ls -lah /var/log
```

- `ls` 是命令；
- `-l`、`-a`、`-h` 是短选项，并合并写成 `-lah`；
- `/var/log` 是操作对象；
- 长选项通常以两个连字符开头，例如 `ls --all`。

### 3.1 获取帮助

```bash
man ls              # 查看 ls 的手册，man = manual
ls --help           # 查看命令自带的帮助
help cd             # 查看 Bash 内建命令 cd 的帮助
apropos permission  # 按关键词搜索手册
```

阅读 `man` 手册时常用按键：

- `Space`：下一页；
- `b`：上一页；
- `/关键词`：向后搜索；
- `n`：跳到下一个匹配项；
- `q`：退出。

### 3.2 常用终端快捷键

- `Tab`：补全命令或路径；
- `↑`、`↓`：浏览历史命令；
- `Ctrl + C`：向前台进程发送中断信号；
- `Ctrl + D`：发送输入结束标志，也可退出当前 Shell；
- `Ctrl + L`：清屏，效果类似 `clear`；
- `Ctrl + A`：移动到行首；
- `Ctrl + E`：移动到行尾；
- `Ctrl + R`：反向搜索历史命令；
- `Ctrl + Z`：暂停当前前台进程。

## 4. Linux 目录结构

Linux 只有一棵目录树，最顶层是根目录 `/`。其他磁盘或分区通常被挂载到这棵树的某个目录下，不使用 Windows 式的 `C:`、`D:` 盘符。

| 目录 | 英文含义 | 主要用途 |
| --- | --- | --- |
| `/` | root | 整个文件系统的根目录 |
| `/home` | home | 普通用户的主目录，例如 `/home/alice` |
| `/root` | root user's home | root 用户的主目录，不是根目录 `/` |
| `/etc` | 常解释为 editable text configuration | 系统和软件的配置文件 |
| `/bin` | binaries | 基本命令的可执行文件；现代 Ubuntu 中常链接到 `/usr/bin` |
| `/sbin` | system binaries | 系统管理命令；现代 Ubuntu 中常链接到 `/usr/sbin` |
| `/usr` | Unix system resources | 大量只读程序、库和共享资源 |
| `/var` | variable | 经常变化的数据，如日志、缓存和队列 |
| `/tmp` | temporary | 临时文件，可能在重启或定期清理时被删除 |
| `/dev` | devices | 设备文件 |
| `/proc` | processes | 进程和内核信息的虚拟文件系统 |
| `/sys` | system | 设备和内核对象的虚拟文件系统 |
| `/run` | runtime | 系统启动后的运行时状态数据 |
| `/boot` | boot | 内核及启动相关文件 |
| `/mnt` | mount | 临时挂载文件系统的位置 |
| `/media` | media | U 盘等可移动介质的常用挂载位置 |
| `/opt` | optional | 可选的第三方软件 |
| `/srv` | service | 服务对外提供的数据 |

> `/etc` 的名称来源存在历史争议，不必强行记成唯一缩写。学习命令缩写时，也应注意有些名称是单词截取、历史名称或作者姓名，并不一定是严格首字母缩写。

## 5. 路径与目录操作

### 5.1 绝对路径和相对路径

- 绝对路径从 `/` 开始，例如 `/home/alice/app/main.py`；
- 相对路径以当前目录为参照，例如 `app/main.py`；
- `.` 表示当前目录；
- `..` 表示上一级目录；
- `~` 表示当前用户的主目录；
- `-` 在 `cd -` 中表示上一次所在目录。

### 5.2 常用目录命令

```bash
pwd                  # 显示当前目录
ls                   # 列出目录内容
ls -lah              # 详细显示，包括隐藏文件，并使用易读单位
cd /var/log          # 进入指定目录
cd ..                # 返回上一级目录
cd ~                 # 回到当前用户主目录
cd -                 # 返回上一次所在目录
mkdir demo           # 创建目录
mkdir -p a/b/c       # 连同缺少的父目录一起创建
rmdir empty_dir      # 删除空目录
```

命令名称来源：

- `pwd` = **print working directory**，打印当前工作目录；
- `ls` = **list**，列出内容；
- `cd` = **change directory**，切换目录；
- `mkdir` = **make directory**，创建目录；
- `rmdir` = **remove directory**，删除目录。

隐藏文件的名称以 `.` 开头，例如 `.bashrc`。默认 `ls` 不显示隐藏文件，需要使用 `ls -a`，其中 `a` 表示 **all**。

## 6. 文件的创建、复制、移动和删除

```bash
touch notes.txt              # 创建空文件；存在时通常更新时间戳
cp source.txt backup.txt     # 复制文件
cp -r src src_backup         # 递归复制目录
mv old.txt new.txt           # 重命名文件
mv file.txt ./archive/       # 移动文件
rm file.txt                  # 删除文件
rm -r old_dir                # 递归删除目录
rm -i important.txt          # 删除前询问
ln source.txt hard-link.txt  # 创建硬链接
ln -s source.txt link.txt    # 创建符号链接
file image.png               # 判断文件类型
stat notes.txt               # 查看文件的详细元数据
```

名称来源：

- `cp` = **copy**；
- `mv` = **move**；
- `rm` = **remove**；
- `ln` = **link**；
- `stat` = **status**。

> `rm` 删除的文件通常不会进入桌面回收站。尤其要谨慎使用 `rm -r`、`rm -f` 和管理员权限。执行删除前，可先用 `pwd`、`ls` 确认当前位置和目标。

### 6.1 通配符

通配符由 Shell 在命令执行前展开：

```bash
ls *.py             # 匹配所有 .py 文件
ls file?.txt        # ? 匹配任意一个字符
ls file[0-9].txt    # 匹配 file0.txt 到 file9.txt
```

- `*`：匹配任意数量的字符；
- `?`：匹配一个字符；
- `[abc]`：匹配集合中的一个字符；
- `[0-9]`：匹配指定范围内的一个字符。

### 6.2 引号和转义

```bash
touch "my notes.txt"       # 双引号保留空格，但仍允许变量展开
echo '$HOME'               # 单引号中的内容按字面值处理
echo "$HOME"              # 输出 HOME 变量的值
touch my\ notes.txt        # 反斜杠转义空格
```

文件名包含空格时，应使用引号或反斜杠转义。

## 7. 查看和处理文本

Linux 的配置、日志和源代码大多是文本，因此文本处理命令非常重要。

```bash
cat file.txt                # 输出文件内容
less large.log              # 分页查看大文件
head -n 20 file.txt         # 查看前 20 行
tail -n 20 file.txt         # 查看后 20 行
tail -f app.log             # 持续跟踪新增日志
wc -l file.txt              # 统计行数
sort names.txt              # 对行进行排序
uniq names.txt              # 去除相邻重复行
cut -d ':' -f 1 /etc/passwd # 以 : 分列，取第 1 列
tr 'a-z' 'A-Z'              # 将小写字符转换成大写
```

名称来源：

- `cat` = **concatenate**，原意是连接文件，也常用于显示文件；
- `less`：是对早期分页工具 `more` 的改进，名称来自“less is more”的双关；
- `head`：文件开头；
- `tail`：文件末尾；
- `wc` = **word count**，可统计行、单词和字节数；
- `uniq` = **unique**；
- `cut`：切取文本列；
- `tr` = **translate** 或 **transliterate**，转换字符。

### 7.1 搜索文本：grep

`grep` 常解释为 **global regular expression print**，用于按模式筛选文本行。

```bash
grep "error" app.log          # 查找包含 error 的行
grep -i "error" app.log       # 忽略大小写
grep -n "error" app.log       # 显示行号
grep -r "TODO" ./src          # 递归搜索目录
grep -v "debug" app.log       # 显示不匹配的行
grep -E "error|warning" app.log # 使用扩展正则表达式
```

常见选项：

- `-i` = ignore case，忽略大小写；
- `-n` = line number，显示行号；
- `-r` = recursive，递归搜索；
- `-v` = invert match，反向匹配；
- `-E` = extended regular expression，扩展正则表达式。

### 7.2 sed 和 awk

`sed` 是 **stream editor**（流编辑器），适合按行替换、删除或选择文本：

```bash
sed 's/old/new/' file.txt       # 每行替换第一个 old，仅输出结果
sed 's/old/new/g' file.txt      # 替换每行所有 old
sed -n '10,20p' file.txt        # 输出第 10 到 20 行
```

`awk` 适合按字段处理结构化文本，名称来自三位作者 Aho、Weinberger、Kernighan 的姓氏首字母：

```bash
awk '{print $1}' file.txt
awk -F ':' '{print $1, $7}' /etc/passwd
```

其中 `$1` 表示第一列，`$2` 表示第二列，`$0` 表示整行。

## 8. 标准输入、标准输出、重定向与管道

Linux 进程通常有三个标准数据流：

| 编号 | 名称 | 缩写 | 默认位置 |
| --- | --- | --- | --- |
| `0` | 标准输入 | stdin | 键盘 |
| `1` | 标准输出 | stdout | 终端 |
| `2` | 标准错误 | stderr | 终端 |

### 8.1 重定向

```bash
echo "hello" > hello.txt       # 覆盖写入标准输出
echo "again" >> hello.txt      # 追加标准输出
command 2> error.log            # 将标准错误写入文件
command > output.log 2>&1       # 标准输出和错误写入同一文件
sort < names.txt                # 从文件读取标准输入
```

`>` 会覆盖文件，`>>` 会追加内容。使用 `>` 前应确认目标文件是否允许被覆盖。

### 8.2 管道

管道 `|` 把前一个命令的标准输出交给后一个命令作为标准输入：

```bash
cat app.log | grep "ERROR" | wc -l
```

这表示统计日志中包含 `ERROR` 的行数。因为 `grep` 可以直接读取文件，也可以简化为：

```bash
grep "ERROR" app.log | wc -l
```

### 8.3 tee

`tee` 的名字来自 T 形水管，它把输入同时输出到屏幕和文件：

```bash
command | tee result.txt
command | tee -a result.txt     # 同时追加到文件
```

## 9. 查找文件与命令

```bash
find . -name "*.py"                  # 按名称查找
find /var/log -type f -size +10M      # 查找大于 10 MiB 的普通文件
find . -type f -mtime -7              # 查找 7 天内修改过的文件
locate nginx.conf                      # 查询文件名数据库
which python3                          # 查找 PATH 中将执行的程序
whereis python3                        # 查找程序、源码和手册的大致位置
type cd                                # 判断名称是别名、内建命令还是外部程序
```

- `find` 实时遍历目录，结果准确但可能较慢；
- `locate` 查询预先建立的数据库，速度快但结果可能不是最新；
- `which` 主要按 `PATH` 查找可执行程序；
- `type` 是判断命令实际来源的可靠方式之一。

Ubuntu 如未安装 `locate`，可执行：

```bash
sudo apt install plocate
sudo updatedb
```

## 10. 用户、用户组与权限

### 10.1 用户身份

```bash
whoami              # 显示当前有效用户名
id                  # 显示用户 ID、组 ID 和所属组
who                 # 显示当前登录用户
groups               # 显示当前用户所属组
```

- `uid` = **user identifier**，用户标识；
- `gid` = **group identifier**，用户组标识；
- root 用户的 UID 通常是 `0`。

### 10.2 读取权限字符串

执行 `ls -l` 可能看到：

```text
-rwxr-x--- 1 alice developers 1024 Jul 24 10:00 deploy.sh
```

第一部分可以拆分为：

```text
-  rwx  r-x  ---
│   │    │    └─ 其他用户（others）的权限
│   │    └────── 所属组（group）的权限
│   └─────────── 所有者（user）的权限
└─────────────── 文件类型：- 普通文件，d 目录，l 符号链接
```

三种基本权限：

- `r` = **read**，读取；
- `w` = **write**，写入；
- `x` = **execute**，执行。

对目录来说，`r` 表示列出名称，`w` 表示创建或删除目录项，`x` 表示进入和访问目录中的对象。

### 10.3 修改权限和所有者

```bash
chmod u+x script.sh             # 给所有者增加执行权限
chmod g-w file.txt              # 移除所属组的写权限
chmod o=r file.txt              # 将其他用户权限设为只读
chmod 755 script.sh             # rwxr-xr-x
chmod 644 config.txt            # rw-r--r--
chown alice file.txt            # 修改所有者
chown alice:developers file.txt # 同时修改所有者和所属组
chgrp developers file.txt       # 修改所属组
```

名称来源：

- `chmod` = **change mode**；
- `chown` = **change owner**；
- `chgrp` = **change group**。

数字权限中：

- `r = 4`；
- `w = 2`；
- `x = 1`。

因此 `7 = 4 + 2 + 1 = rwx`，`5 = 4 + 1 = r-x`，`4 = r--`。

> 不建议为了省事对文件使用 `chmod 777`。它会允许所有用户读、写、执行，通常超出实际需要。应遵循最小权限原则。

### 10.4 sudo 与 root

`sudo` 通常解释为 **superuser do**，Ubuntu 使用它让被授权的普通用户临时以更高权限执行单条命令：

```bash
sudo apt update
sudo systemctl restart nginx
```

输入密码时终端不会显示星号，这是正常的安全设计。不要在不理解命令作用时使用 `sudo`，因为管理员权限可以修改或破坏整个系统。

## 11. Ubuntu 软件包管理

Ubuntu 基于 Debian，常见的包管理层次是：

```text
apt（面向用户的高级包管理命令）
  ↓
dpkg（处理本地 .deb 软件包）
  ↓
文件被安装到系统目录
```

- `APT` = **Advanced Package Tool**；
- `dpkg` = **Debian package**；
- `.deb` = Debian 软件包格式。

### 11.1 apt 常用命令

```bash
sudo apt update                 # 更新可用软件包索引，不是升级软件
apt list --upgradable           # 查看可升级的软件
sudo apt upgrade                # 升级已安装的软件包
sudo apt install git            # 安装软件
sudo apt remove git             # 删除软件，通常保留配置
sudo apt purge git              # 删除软件及其系统配置
sudo apt autoremove             # 删除不再需要的自动依赖
apt search nginx                # 搜索软件包
apt show nginx                  # 查看软件包信息
```

`apt update` 只刷新“仓库里有哪些版本”的本地索引，`apt upgrade` 才真正安装升级。

### 11.2 dpkg 常用命令

```bash
sudo dpkg -i package.deb        # 安装本地 deb 包
dpkg -l                         # 列出已安装的软件包
dpkg -L package-name            # 查看某个包安装了哪些文件
dpkg -S /usr/bin/python3        # 查询文件属于哪个软件包
```

直接用 `dpkg -i` 安装时可能缺少依赖，可在之后运行：

```bash
sudo apt --fix-broken install
```

## 12. 进程与作业管理

程序运行后会形成进程（Process）。每个进程都有进程 ID，即 PID（**process identifier**）。内核负责在进程之间分配 CPU 时间和内存。

```bash
ps                      # 查看当前终端相关进程
ps aux                  # 查看系统中的详细进程列表
top                     # 动态查看进程和系统负载
pgrep -a python         # 按名称查找进程并显示命令行
pidof nginx             # 查询程序的 PID
kill 1234               # 默认发送 SIGTERM，请求进程正常退出
kill -9 1234            # 发送 SIGKILL，强制结束进程
pkill -f "python app.py" # 按命令行模式结束进程
```

名称来源：

- `ps` = **process status**；
- `PID` = **process identifier**；
- `pgrep` = **process grep**；
- `pkill` = **process kill**；
- `SIGTERM` = **signal terminate**；
- `SIGKILL` = **signal kill**。

`kill` 的本质是“发送信号”，不一定意味着强制杀死。通常先使用默认的 `SIGTERM`，让进程有机会保存数据和清理资源；只有进程无法正常退出时才考虑 `kill -9`。

### 12.1 前台、后台和作业

```bash
python3 app.py &        # 在后台启动
jobs                    # 查看当前 Shell 的作业
fg %1                   # 将 1 号作业切到前台
bg %1                   # 让暂停的 1 号作业在后台继续
nohup command &         # 忽略挂断信号并在后台运行
```

- `fg` = **foreground**，前台；
- `bg` = **background**，后台；
- `nohup` = **no hang up**，不因终端挂断而结束。

对于长期运行的正式服务，应优先使用 systemd、容器或进程管理工具，而不是只使用 `nohup`。

## 13. systemd 服务与系统日志

现代 Ubuntu 通常使用 systemd 作为初始化系统和服务管理器。PID 为 `1` 的 systemd 在系统启动后负责启动和管理其他系统服务。

```bash
systemctl status nginx          # 查看服务状态
sudo systemctl start nginx      # 启动服务
sudo systemctl stop nginx       # 停止服务
sudo systemctl restart nginx    # 重启服务
sudo systemctl reload nginx     # 重新加载配置，服务不一定中断
sudo systemctl enable nginx     # 设置开机启动
sudo systemctl disable nginx    # 取消开机启动
sudo systemctl enable --now nginx # 立即启动并设置开机启动
```

`systemctl` 可理解为 **system control**。systemd 管理的服务单元通常以 `.service` 结尾。

### 13.1 journalctl 查看日志

```bash
journalctl -u nginx             # 查看 nginx 服务日志
journalctl -u nginx -f          # 持续跟踪日志
journalctl -b                   # 查看本次启动以来的日志
journalctl -p err               # 只查看错误级别日志
journalctl --since "1 hour ago" # 查看最近一小时日志
```

`journalctl` 表示控制和查询 systemd journal。许多传统文本日志仍可在 `/var/log` 下找到。

## 14. 磁盘、文件系统与空间

磁盘上的分区经过格式化后形成文件系统，例如 ext4。文件系统必须被**挂载（mount）**到某个目录，用户才能通过 Linux 的目录树访问它。

```bash
df -h                 # 查看已挂载文件系统的空间
du -sh ./project      # 统计目录占用空间
du -h --max-depth=1   # 查看当前目录下各一级目录的大小
lsblk                 # 列出块设备
blkid                 # 查看块设备的 UUID 和文件系统类型
mount                 # 查看挂载情况
findmnt               # 以树状结构查看挂载点
```

名称来源：

- `df` = **disk free**，显示文件系统剩余空间；
- `du` = **disk usage**，统计文件或目录占用；
- `lsblk` = **list block devices**；
- `blkid` = **block identifier**；
- `UUID` = **universally unique identifier**。

`df` 和 `du` 的结果可能不同：`df` 从文件系统整体角度统计，`du` 遍历可见文件统计。文件被删除但仍被进程打开时，其空间会体现在 `df` 中，却不一定体现在 `du` 中。

## 15. 压缩与归档

归档是把多个文件打包成一个文件，压缩则是减少数据体积。`tar` 最初表示 **tape archive**（磁带归档）。

```bash
tar -cvf archive.tar folder/       # 创建未压缩归档
tar -xvf archive.tar               # 解开 tar 归档
tar -czvf archive.tar.gz folder/   # 使用 gzip 压缩并归档
tar -xzvf archive.tar.gz           # 解开 tar.gz
tar -cJvf archive.tar.xz folder/   # 使用 xz 压缩并归档
tar -xJvf archive.tar.xz           # 解开 tar.xz
zip -r archive.zip folder/         # 创建 zip 文件
unzip archive.zip                  # 解压 zip 文件
```

`tar` 常用选项：

- `-c` = create，创建；
- `-x` = extract，提取；
- `-v` = verbose，显示详细过程；
- `-f` = file，指定归档文件，后面应紧跟文件名；
- `-z` = gzip；
- `-J` = xz。

## 16. 网络基础与常用命令

### 16.1 基本概念

- IP 地址：设备在网络中的地址；
- 端口（Port）：一台主机上区分不同网络服务的编号；
- DNS = **Domain Name System**，把域名解析成 IP 地址；
- TCP = **Transmission Control Protocol**，可靠的面向连接协议；
- UDP = **User Datagram Protocol**，轻量、无连接的数据报协议；
- localhost：本机，通常对应 IPv4 地址 `127.0.0.1`；
- `0.0.0.0`：服务监听时通常表示所有 IPv4 网络接口，不是供浏览器访问的具体目标地址。

### 16.2 网络诊断

```bash
ip addr                         # 查看网络接口和 IP 地址
ip route                        # 查看路由表
ping -c 4 8.8.8.8               # 测试 IP 连通性
ping -c 4 ubuntu.com            # 同时检查 DNS 和网络连通性
ss -lntp                        # 查看监听中的 TCP 端口及相关进程
curl -I https://ubuntu.com      # 获取 HTTP 响应头
curl https://example.com        # 请求并输出网页内容
wget https://example.com/a.zip  # 下载文件
dig ubuntu.com                  # 查询 DNS，可能需安装 dnsutils
hostname                        # 显示主机名
hostname -I                     # 显示本机 IP 地址
```

名称来源：

- `ip` = Internet Protocol；
- `ping` 的名字来自声呐“乒”的回声，也常被反向解释为 packet internet groper；
- `ss` = **socket statistics**；
- `curl` = **client URL**；
- `wget` = **web get**；
- `dig` = **domain information groper**；
- `DNS` = **Domain Name System**。

### 16.3 SSH 远程连接

`SSH` = **Secure Shell**，用于加密的远程登录和命令执行：

```bash
ssh alice@192.168.1.10
ssh -p 2222 alice@example.com
ssh-keygen -t ed25519
ssh-copy-id alice@192.168.1.10
scp file.txt alice@server:/tmp/
rsync -av project/ alice@server:/srv/project/
```

- `scp` = **secure copy**；
- `rsync` = **remote synchronization**；
- `ssh-keygen` = SSH key generator。

SSH 密钥通常包含私钥和公钥。私钥留在本机并妥善保护，公钥可以放到服务器。不要通过聊天、邮件或代码仓库公开私钥。

## 17. 环境变量、PATH 与 Shell 配置

环境变量是进程可读取的“名称—值”数据。子进程通常继承父进程导出的环境变量。

```bash
env                         # 查看所有已导出的环境变量
echo "$HOME"                # 查看主目录变量
echo "$PATH"                # 查看命令搜索路径
export APP_ENV=development  # 设置并导出环境变量
unset APP_ENV               # 删除变量
```

`PATH` 是用冒号分隔的目录列表。输入一个不含 `/` 的命令时，Shell 会按顺序到这些目录中查找可执行文件：

```bash
echo "$PATH"
command -v python3
```

当前目录通常不在 `PATH` 中，因此运行当前目录下的脚本时要写：

```bash
./script.sh
```

其中 `./` 明确表示“当前目录中的”。

### 17.1 Bash 配置文件

Ubuntu 中常见文件：

- `~/.bashrc`：交互式非登录 Bash 常读取；
- `~/.profile`：登录时常读取，可设置环境变量；
- `/etc/environment`：系统级环境变量配置之一；
- `/etc/profile`：系统级登录 Shell 配置。

修改 `~/.bashrc` 后，可以重新打开终端，也可以执行：

```bash
source ~/.bashrc
```

`source` 在当前 Shell 中读取并执行文件；若直接运行脚本，通常会创建子进程，变量不会反向影响父 Shell。

### 17.2 alias 别名

```bash
alias ll='ls -alF'
alias gs='git status'
unalias gs
```

若希望别名长期有效，可将定义写入 `~/.bashrc`。

## 18. Shell 脚本基础

Shell 脚本把一系列命令保存到文件中，便于重复执行。

```bash
#!/usr/bin/env bash

set -e
name="Ubuntu"
echo "Hello, $name"
```

第一行叫 shebang：

- `#!` 告诉内核使用哪个解释器；
- `/usr/bin/env bash` 通过 `PATH` 查找 Bash。

运行脚本：

```bash
chmod u+x hello.sh
./hello.sh
```

或不增加执行权限，直接让 Bash 读取：

```bash
bash hello.sh
```

### 18.1 命令退出状态

Linux 命令结束时会返回退出状态：通常 `0` 表示成功，非 `0` 表示失败。

```bash
command
echo "$?"                 # 查看上一条命令的退出状态

mkdir demo && cd demo     # 前一条成功才执行后一条
test -f config.txt || echo "config.txt 不存在"
```

- `&&`：前一个命令成功时才继续；
- `||`：前一个命令失败时才继续；
- `;`：无论前一个命令是否成功，都继续执行下一条。

## 19. 时间、系统与硬件信息

```bash
date                    # 查看日期时间
timedatectl              # 查看时区和时间同步状态
uname -a                # 查看内核和系统信息
cat /etc/os-release     # 查看 Ubuntu 发行版信息
lsb_release -a          # 查看发行版信息，部分系统需安装 lsb-release
uptime                  # 查看运行时长和平均负载
free -h                 # 查看内存使用情况
lscpu                   # 查看 CPU 信息
hostnamectl             # 查看或管理主机信息
```

名称来源：

- `uname` = **Unix name**；
- `uptime`：系统已运行时间；
- `free`：内存空闲和使用情况；
- `lscpu` = **list CPU**；
- `LSB` = **Linux Standard Base**。

`free` 输出中的 `available` 比 `free` 列更能反映应用还可使用多少内存，因为 Linux 会主动把空闲内存用于文件缓存，并在应用需要时回收。

## 20. 一般开发者常用操作

### 20.1 Git

```bash
sudo apt update
sudo apt install git
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 20.2 Python

Ubuntu 的系统工具可能依赖系统 Python，不建议随意删除或覆盖 `/usr/bin/python3`。开发项目可使用虚拟环境：

```bash
sudo apt install python3 python3-venv python3-pip
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install requests
deactivate
```

虚拟环境为每个项目提供相对独立的 Python 解释器和依赖目录，减少不同项目之间的版本冲突。

### 20.3 编译工具

```bash
sudo apt install build-essential
gcc --version
make --version
```

Ubuntu 的 `build-essential` 元软件包通常会安装 GCC、G++、make 和必要的开发文件：

- `GCC` = **GNU Compiler Collection**；
- `GNU` = **GNU's Not Unix**，是递归缩写；
- `make` 根据 Makefile 中的规则组织构建。

## 21. 常见排查思路

### 21.1 command not found

看到 `command not found` 时，可依次检查：

```bash
type command_name
command -v command_name
echo "$PATH"
apt search command_name
```

常见原因包括：命令未安装、名称拼错、程序目录不在 `PATH` 中，或脚本缺少执行权限。

### 21.2 Permission denied

检查：

```bash
ls -l target
id
namei -l /full/path/to/target
```

可能是文件没有执行权限、当前用户没有读写权限，或路径上某一级目录没有 `x` 权限。不要一看到权限错误就使用 `sudo` 或 `chmod 777`，应先找到缺少的具体权限。

### 21.3 磁盘空间不足

```bash
df -h
df -i                         # 查看 inode 是否耗尽
du -h --max-depth=1 /var 2>/dev/null | sort -h
sudo journalctl --disk-usage
```

空间不足可能是文件内容占满，也可能是大量小文件耗尽 inode。`inode` 是文件系统记录文件元数据的数据结构。

### 21.4 端口已被占用

```bash
sudo ss -lntp
sudo ss -lntp '( sport = :8080 )'
```

找到占用端口的 PID 后，先确认它是什么服务，再决定停止服务或修改应用端口。

### 21.5 服务启动失败

```bash
systemctl status service-name
journalctl -u service-name -n 100 --no-pager
```

重点查看最早出现的明确错误，例如配置语法错误、文件不存在、权限不足或端口冲突，而不是只看最后一行“启动失败”。

## 22. 安全和操作习惯

1. 日常使用普通用户，只在必要时对单条命令使用 `sudo`。
2. 执行删除、移动、覆盖命令前，用 `pwd` 和 `ls` 确认目标。
3. 重要数据在修改前备份，并验证备份能否恢复。
4. 不运行来源不明的脚本，尤其是 `curl ... | sudo bash` 形式的命令。
5. 不把密码、SSH 私钥、API 密钥提交到 Git 仓库。
6. 定期执行 `sudo apt update` 和 `sudo apt upgrade` 安装安全更新。
7. 服务只监听必要的网络接口，只开放必要的端口。
8. 使用最小权限，不用 `chmod 777` 代替权限分析。
9. 复制网上命令前，先通过 `man`、`--help` 理解选项。
10. 生产环境变更应记录步骤，并提前准备回滚方法。

## 23. 常用命令速查表

| 命令 | 英文来源或含义 | 用途 |
| --- | --- | --- |
| `pwd` | print working directory | 显示当前目录 |
| `ls` | list | 列出目录内容 |
| `cd` | change directory | 切换目录 |
| `mkdir` | make directory | 创建目录 |
| `rmdir` | remove directory | 删除空目录 |
| `cp` | copy | 复制 |
| `mv` | move | 移动或重命名 |
| `rm` | remove | 删除 |
| `ln` | link | 创建链接 |
| `cat` | concatenate | 连接或显示文件 |
| `wc` | word count | 统计行、词、字节 |
| `grep` | global regular expression print | 按模式搜索文本 |
| `sed` | stream editor | 流式编辑文本 |
| `awk` | 三位作者姓氏首字母 | 按字段处理文本 |
| `chmod` | change mode | 修改权限 |
| `chown` | change owner | 修改所有者 |
| `chgrp` | change group | 修改所属组 |
| `ps` | process status | 查看进程 |
| `kill` | 发送信号 | 通知或终止进程 |
| `df` | disk free | 查看文件系统空间 |
| `du` | disk usage | 统计文件占用空间 |
| `tar` | tape archive | 归档文件 |
| `ssh` | secure shell | 安全远程登录 |
| `scp` | secure copy | 通过 SSH 复制文件 |
| `ss` | socket statistics | 查看网络套接字 |
| `ip` | Internet Protocol | 查看和配置网络 |
| `apt` | Advanced Package Tool | Ubuntu 软件包管理 |
| `dpkg` | Debian package | 管理 `.deb` 包 |
| `sudo` | superuser do | 临时使用管理员权限 |
| `systemctl` | system control | 管理 systemd 服务 |
| `journalctl` | journal control | 查询 systemd 日志 |
| `env` | environment | 查看环境变量 |
| `man` | manual | 查看命令手册 |

## 24. 推荐学习顺序

初学时不必一次记住所有选项，可以按以下顺序练习：

1. 使用 `pwd`、`ls`、`cd` 熟悉目录树；
2. 使用 `mkdir`、`touch`、`cp`、`mv`、`rm` 操作练习文件；
3. 使用 `cat`、`less`、`grep`、`head`、`tail` 阅读文本和日志；
4. 理解标准输入、标准输出、重定向和管道；
5. 学习用户、用户组、`rwx` 权限和 `sudo`；
6. 使用 `apt` 安装和升级软件；
7. 使用 `ps`、`top`、`kill` 理解进程；
8. 使用 `systemctl`、`journalctl` 管理和排查服务；
9. 使用 `ip`、`ss`、`curl`、`ssh` 处理网络问题；
10. 把重复操作写成简单的 Shell 脚本。

真正掌握 Linux 的关键不是背诵全部命令，而是理解目录、权限、进程、输入输出和网络这些基础模型，并养成查阅 `man` 手册、阅读错误信息和逐步验证的习惯。
