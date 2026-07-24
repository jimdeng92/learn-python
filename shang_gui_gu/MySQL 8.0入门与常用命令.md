# MySQL 8.0 入门与常用命令

本文面向 MySQL 初学者和一般开发者，基于 **MySQL 8.0** 介绍关系型数据库的基本原理、安装与连接、SQL 语法、索引、事务、用户权限、备份恢复和常见问题排查。

文中的系统管理示例主要使用 Ubuntu。不同 Ubuntu 小版本、MySQL 8.0 小版本或安装来源之间，配置文件位置和默认设置可能略有差异。

## 1. MySQL 是什么

MySQL 是一种关系型数据库管理系统：

- `DB` = **Database**，数据库；
- `DBMS` = **Database Management System**，数据库管理系统；
- `RDBMS` = **Relational Database Management System**，关系型数据库管理系统；
- `SQL` = **Structured Query Language**，结构化查询语言。

关系型数据库使用表保存数据。表由行和列组成：

- 表（Table）：同一类数据的集合，例如用户表；
- 行（Row）：一条完整记录，例如一个用户；
- 列（Column）：记录的一个属性，例如用户名；
- 主键（Primary Key）：唯一标识一行数据；
- 外键（Foreign Key）：引用另一张表的主键或唯一键；
- 模式（Schema）：数据库对象的逻辑组织。在 MySQL 中，`SCHEMA` 基本等同于 `DATABASE`。

MySQL 8.0 默认使用 InnoDB 存储引擎。InnoDB 支持事务、行级锁、崩溃恢复和外键，是一般业务系统的首选。

## 2. MySQL 的工作结构

MySQL 使用客户端—服务器架构：

```text
应用程序 / mysql 命令行客户端
          ↓ TCP 或 Unix Socket
MySQL Server
  ├─ 连接与权限验证
  ├─ SQL 解析器
  ├─ 查询优化器
  ├─ 执行器
  └─ InnoDB 存储引擎
          ↓
       数据文件
```

### 2.1 客户端与服务器

- MySQL Server 是长期运行的数据库服务进程，程序名通常是 `mysqld`；
- `mysql` 是命令行客户端，用来连接服务器并发送 SQL；
- 应用程序也可通过 Connector、Driver 等数据库驱动连接服务器；
- 默认 TCP 端口是 `3306`；
- 本机还可以通过 Unix Socket 文件连接。

`mysqld` 中的 `d` 表示 **daemon**，即在后台长期运行的守护进程。

### 2.2 一条 SELECT 的大致执行过程

当客户端发送一条查询时，MySQL 大致执行以下步骤：

1. 验证连接用户及其权限；
2. 解析 SQL，检查语法并建立语法树；
3. 优化器比较可行的执行计划，例如使用哪个索引、表按什么顺序连接；
4. 执行器根据计划向 InnoDB 请求数据；
5. InnoDB 从缓冲池或磁盘读取数据；
6. 服务器把结果集返回客户端。

优化器会选择它估计成本较低的执行计划，但估算依赖统计信息，不保证在所有场景下都是人类认为的最优方案。

## 3. MySQL 8.0 的主要特点

与较老版本相比，MySQL 8.0 常用的重要能力包括：

- 默认字符集为 `utf8mb4`，能完整存储 Unicode 和 emoji；
- 支持窗口函数；
- 支持公共表表达式 CTE；
- 支持递归 CTE；
- 支持更完善的 JSON 操作；
- 默认身份验证插件通常为 `caching_sha2_password`；
- 数据字典由 InnoDB 统一管理；
- 支持降序索引、不可见索引和表达式索引；
- `EXPLAIN ANALYZE` 可以实际执行并分析查询；
- 原子 DDL 改善了部分结构变更的可靠性。

其中：

- `CTE` = **Common Table Expression**，公共表表达式；
- `JSON` = **JavaScript Object Notation**；
- `DDL` = **Data Definition Language**，数据定义语言。

## 4. 在 Ubuntu 安装和管理 MySQL 8.0

### 4.1 安装前确认版本

Ubuntu 自带软件源提供的版本取决于 Ubuntu 版本。安装前先查看候选版本：

```bash
sudo apt update
apt policy mysql-server
```

如果候选版本为 `8.0.x`，可直接安装：

```bash
sudo apt install mysql-server
```

如果 Ubuntu 软件源提供的不是 MySQL 8.0，应使用 MySQL 官方 APT 仓库，并按照官方对应 Ubuntu 版本的说明安装。不要仅为了固定版本随意添加来源不明的软件源。

### 4.2 管理服务

```bash
sudo systemctl status mysql
sudo systemctl start mysql
sudo systemctl stop mysql
sudo systemctl restart mysql
sudo systemctl enable mysql
sudo systemctl enable --now mysql
```

- `systemctl` 可理解为 **system control**；
- `start`：启动；
- `stop`：停止；
- `restart`：停止后重新启动；
- `enable`：设置开机启动；
- `--now`：设置开机启动的同时立即启动。

### 4.3 查看版本

在系统终端中执行：

```bash
mysql --version
mysqld --version
```

连接 MySQL 后执行：

```sql
SELECT VERSION();
```

本文目标版本应显示为 `8.0.x`。其中 `x` 是具体补丁版本，例如 `8.0.36`。

### 4.4 初始安全设置

部分安装方式可以运行：

```bash
sudo mysql_secure_installation
```

该工具可以帮助设置密码策略、移除匿名用户、限制远程 root 登录和删除测试数据库。每个问题应根据实际环境选择，而不是机械地全部回答 `Y`。

Ubuntu 软件源安装的 MySQL 可能允许系统 root 用户通过本地 Socket 登录：

```bash
sudo mysql
```

这不等于 MySQL 的 root 用户没有安全限制，而是可能使用 `auth_socket` 插件将操作系统身份映射为数据库身份。

## 5. 连接 MySQL

### 5.1 mysql 客户端参数

```bash
mysql -u root -p
mysql -h 127.0.0.1 -P 3306 -u app_user -p
mysql -h db.example.com -P 3306 -u app_user -p app_db
```

参数含义：

- `-u` = **user**，用户名；
- `-p` = **password**，提示输入密码；
- `-h` = **host**，服务器地址；
- `-P` = **port**，TCP 端口，注意是大写 `P`；
- 最后的 `app_db` 是连接后默认使用的数据库。

不要写成下面这样：

```bash
mysql -u app_user -pMyPlainTextPassword
```

把密码直接放在命令行中可能被 Shell 历史、进程列表或日志记录。更安全的做法是只写 `-p`，然后交互输入。

### 5.2 localhost 与 127.0.0.1 的区别

在 Linux 上：

- `mysql -h localhost` 通常优先使用 Unix Socket；
- `mysql -h 127.0.0.1` 明确使用 TCP；
- 两者连接的虽然通常是同一台机器，但连接方式和 MySQL 账户匹配结果可能不同。

MySQL 账户由“用户名 + 来源主机”共同组成，例如：

```text
'app_user'@'localhost'
'app_user'@'10.%'
```

它们是两个不同的账户。

### 5.3 mysql 客户端内部命令

连接后可以使用：

```text
help;                查看帮助
status;              查看当前连接状态
show databases;      查看数据库
use app_db;          切换数据库
source init.sql;     执行 SQL 文件
delimiter $$         修改语句分隔符
\c                   取消当前尚未执行的输入
\G                   纵向显示查询结果
quit                 退出
exit                 退出
```

例如：

```sql
SELECT * FROM users WHERE id = 1\G
```

`\G` 适合纵向查看列很多的一行数据。SQL 通常以分号 `;` 结尾，如果忘记分号，客户端会等待继续输入。

## 6. SQL 的分类和缩写

SQL 命令常按作用分为：

| 分类 | 英文全称 | 主要用途 | 常见命令 |
| --- | --- | --- | --- |
| DDL | Data Definition Language | 定义数据库结构 | `CREATE`、`ALTER`、`DROP`、`TRUNCATE` |
| DML | Data Manipulation Language | 修改表中的数据 | `INSERT`、`UPDATE`、`DELETE` |
| DQL | Data Query Language | 查询数据 | `SELECT` |
| DCL | Data Control Language | 用户和权限控制 | `GRANT`、`REVOKE` |
| TCL | Transaction Control Language | 控制事务 | `COMMIT`、`ROLLBACK`、`SAVEPOINT` |

这些分类便于学习，但不同资料可能把 `SELECT` 归入广义 DML，分类边界不必过度纠结。

### 6.1 SQL 基本书写习惯

```sql
SELECT id, username
FROM users
WHERE status = 'active'
ORDER BY created_at DESC;
```

- SQL 关键字通常不区分大小写，但习惯写成大写；
- 字符串使用单引号；
- 反引号用于引用表名或列名等标识符；
- 每条语句以分号结束；
- 生产代码应使用参数化查询，不要拼接用户输入。

## 7. 数据库和表的基本操作

### 7.1 创建和选择数据库

```sql
SHOW DATABASES;

CREATE DATABASE app_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;

USE app_db;
SELECT DATABASE();
DROP DATABASE app_db;
```

- `CHARACTER SET`：字符集，决定字符如何编码；
- `COLLATE`：排序规则，决定字符串如何比较和排序；
- `utf8mb4`：MySQL 中完整的 UTF-8 实现；
- `ai` = **accent insensitive**，不区分重音；
- `ci` = **case insensitive**，不区分大小写。

`DROP DATABASE` 会删除整个数据库及其对象，应先确认数据库名并做好备份。

### 7.2 创建表

```sql
CREATE TABLE users (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    status TINYINT NOT NULL DEFAULT 1,
    profile JSON NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_users_email (email),
    KEY idx_users_status_created_at (status, created_at)
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
```

常见名称约定：

- `pk` = **primary key**，主键；
- `uk` = **unique key**，唯一键；
- `idx` = **index**，普通索引；
- `fk` = **foreign key**，外键。

这些前缀只是团队常用命名约定，并非 MySQL 强制要求。

### 7.3 查看表结构

```sql
SHOW TABLES;
DESCRIBE users;
DESC users;
SHOW CREATE TABLE users\G
```

- `DESC` 在这里是 `DESCRIBE` 的缩写；
- `SHOW CREATE TABLE` 能看到完整建表语句，通常比 `DESC` 更完整。

注意：在 `ORDER BY created_at DESC` 中，`DESC` 表示 **descending**，即降序。它与 `DESC users` 中的 `DESCRIBE` 含义不同，具体由语法位置决定。

### 7.4 修改表结构

```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(30) NULL;
ALTER TABLE users MODIFY COLUMN username VARCHAR(100) NOT NULL;
ALTER TABLE users RENAME COLUMN phone TO mobile;
ALTER TABLE users DROP COLUMN mobile;
RENAME TABLE users TO app_users;
TRUNCATE TABLE app_users;
DROP TABLE app_users;
```

- `ALTER`：修改结构；
- `TRUNCATE`：快速清空整张表，属于 DDL；
- `DROP`：删除对象本身。

在大表上执行 `ALTER TABLE` 可能持有元数据锁、消耗大量 I/O，甚至阻塞业务。生产环境应先了解具体操作是否支持 `INSTANT` 或 `INPLACE`，并制定变更方案。

## 8. 常用数据类型

### 8.1 整数类型

| 类型 | 常见用途 |
| --- | --- |
| `TINYINT` | 小范围整数、状态值 |
| `SMALLINT` | 较小整数 |
| `INT` / `INTEGER` | 一般整数 |
| `BIGINT` | 大范围整数、业务主键 |

`UNSIGNED` 表示无符号，不保存负数，因此正数范围更大。

不要把 `INT(11)` 理解为最多 11 位数字。在 MySQL 8.0 中，整数显示宽度已被弃用或忽略，它不决定存储范围。

### 8.2 精确数值和浮点数

```sql
price DECIMAL(10, 2)
ratio DOUBLE
```

- `DECIMAL(10, 2)` 最多 10 位有效数字，其中 2 位小数，适合金额；
- `FLOAT`、`DOUBLE` 是近似浮点数，可能有二进制精度误差；
- 金额通常使用 `DECIMAL`，不要随意使用浮点数。

### 8.3 字符串类型

| 类型 | 特点 |
| --- | --- |
| `CHAR(n)` | 固定长度，适合长度基本固定的数据 |
| `VARCHAR(n)` | 可变长度，适合普通短文本 |
| `TEXT` | 较长文本 |
| `BLOB` | 二进制大对象 |
| `ENUM` | 从预定义字符串集合中选一个值 |

- `CHAR` = **character**；
- `VARCHAR` = **variable character**；
- `BLOB` = **binary large object**；
- `ENUM` = **enumeration**。

`VARCHAR(n)` 中的 `n` 表示最大字符数，而不是固定的字节数。实际字节数还与字符集和内容有关。

### 8.4 日期和时间

| 类型 | 用途 |
| --- | --- |
| `DATE` | 日期 |
| `TIME` | 时间或时间间隔 |
| `DATETIME` | 日期和时间，不自动按会话时区转换 |
| `TIMESTAMP` | 时间戳，存取时会涉及会话时区转换 |
| `YEAR` | 年份 |

查看时区：

```sql
SELECT @@system_time_zone, @@global.time_zone, @@session.time_zone;
```

跨时区系统常把业务时间统一存为 UTC，并在展示层转换，但具体方案必须结合业务含义。生日等“自然日期”通常不应简单当成 UTC 时间戳。

### 8.5 JSON

MySQL 8.0 原生支持 JSON 类型：

```sql
INSERT INTO users (username, email, profile)
VALUES ('alice', 'alice@example.com', JSON_OBJECT('city', 'Shanghai'));

SELECT profile->>'$.city' AS city
FROM users;
```

JSON 适合保存结构灵活的辅助属性，但不应替代所有关系建模。经常筛选、关联或需要约束的数据，通常更适合独立列或独立表。

## 9. 数据增删改查 CRUD

`CRUD` 表示四种基本数据操作：

- `C` = **Create**，创建；
- `R` = **Read**，读取；
- `U` = **Update**，更新；
- `D` = **Delete**，删除。

### 9.1 INSERT 插入数据

```sql
INSERT INTO users (username, email)
VALUES ('alice', 'alice@example.com');

INSERT INTO users (username, email)
VALUES
    ('bob', 'bob@example.com'),
    ('carol', 'carol@example.com');
```

应明确列名，不依赖表当前的列顺序。

插入或更新唯一键冲突时，可以使用：

```sql
INSERT INTO users (username, email)
VALUES ('alice-new', 'alice@example.com')
AS new
ON DUPLICATE KEY UPDATE username = new.username;
```

`ON DUPLICATE KEY UPDATE` 会在主键或唯一键冲突时转为更新。使用前应确认哪个唯一约束可能触发，避免更新错误记录。

### 9.2 SELECT 查询数据

```sql
SELECT id, username, email
FROM users;

SELECT *
FROM users
WHERE status = 1;
```

生产代码不宜滥用 `SELECT *`：它会读取不需要的列，使网络传输、索引覆盖和字段变更更难控制。

### 9.3 UPDATE 更新数据

```sql
UPDATE users
SET status = 0,
    updated_at = CURRENT_TIMESTAMP
WHERE id = 10;
```

### 9.4 DELETE 删除数据

```sql
DELETE FROM users
WHERE id = 10;
```

执行 `UPDATE` 或 `DELETE` 前，应先用相同的 `WHERE` 条件执行 `SELECT`，确认影响范围：

```sql
SELECT * FROM users WHERE id = 10;
```

缺少 `WHERE` 会影响整张表。

## 10. SELECT 查询详解

### 10.1 条件查询

```sql
SELECT id, username
FROM users
WHERE status = 1
  AND created_at >= '2026-01-01';
```

常见条件：

```sql
WHERE age >= 18
WHERE status <> 0
WHERE id IN (1, 2, 3)
WHERE id BETWEEN 100 AND 200
WHERE email LIKE '%@example.com'
WHERE deleted_at IS NULL
WHERE name IS NOT NULL
```

- `<>` 或 `!=`：不等于；
- `IN`：属于集合；
- `BETWEEN`：包含两端的范围；
- `LIKE`：模式匹配，`%` 匹配任意数量字符，`_` 匹配一个字符；
- 判断空值必须使用 `IS NULL`，不能使用 `= NULL`。

SQL 中的 `NULL` 表示未知或缺失。任何值与 `NULL` 直接比较通常得到未知，而不是 `TRUE`。

### 10.2 排序和分页

```sql
SELECT id, username, created_at
FROM users
ORDER BY created_at DESC, id DESC
LIMIT 20 OFFSET 40;
```

- `ASC` = **ascending**，升序，通常是默认值；
- `DESC` = **descending**，降序；
- `LIMIT`：限制返回行数；
- `OFFSET`：跳过指定行数。

深分页时，较大的 `OFFSET` 可能导致 MySQL 扫描并丢弃大量记录。可以基于上一次结果的排序键进行游标分页：

```sql
SELECT id, username, created_at
FROM users
WHERE (created_at, id) < ('2026-07-24 10:00:00', 1000)
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

### 10.3 去重和别名

```sql
SELECT DISTINCT status FROM users;

SELECT username AS name,
       created_at AS registered_at
FROM users;
```

- `DISTINCT`：去除重复结果；
- `AS`：指定别名，列别名或表别名中可以省略，但显式写出更清晰。

### 10.4 聚合和分组

```sql
SELECT status,
       COUNT(*) AS user_count,
       MIN(created_at) AS first_created_at,
       MAX(created_at) AS last_created_at
FROM users
GROUP BY status
HAVING COUNT(*) >= 10;
```

常见聚合函数：

- `COUNT`：计数；
- `SUM`：求和；
- `AVG` = **average**，平均值；
- `MIN` = **minimum**，最小值；
- `MAX` = **maximum**，最大值。

`WHERE` 在分组前过滤行，`HAVING` 在分组后过滤聚合结果。

`COUNT(*)` 统计行数；`COUNT(column)` 只统计该列非 `NULL` 的行。

### 10.5 SELECT 的逻辑处理顺序

一条查询的逻辑理解顺序通常是：

```text
FROM / JOIN
WHERE
GROUP BY
HAVING
SELECT
DISTINCT
ORDER BY
LIMIT / OFFSET
```

这解释了为什么通常不能在同一层查询的 `WHERE` 中直接使用 `SELECT` 才产生的列别名。

## 11. 表连接 JOIN

假设有订单表：

```sql
CREATE TABLE orders (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id BIGINT UNSIGNED NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_orders_user_id (user_id),
    CONSTRAINT fk_orders_user
        FOREIGN KEY (user_id) REFERENCES users (id)
) ENGINE = InnoDB;
```

### 11.1 INNER JOIN

只返回两边能匹配的记录：

```sql
SELECT u.username, o.id, o.amount
FROM users AS u
INNER JOIN orders AS o ON o.user_id = u.id;
```

`INNER` 表示内部，通常可以省略，直接写 `JOIN`。

### 11.2 LEFT JOIN

返回左表所有记录，右表没有匹配时对应列为 `NULL`：

```sql
SELECT u.id, u.username, o.id AS order_id
FROM users AS u
LEFT JOIN orders AS o ON o.user_id = u.id;
```

查找从未下单的用户：

```sql
SELECT u.id, u.username
FROM users AS u
LEFT JOIN orders AS o ON o.user_id = u.id
WHERE o.id IS NULL;
```

### 11.3 JOIN 的常见问题

- 连接条件遗漏会产生大量笛卡尔积；
- 一对多连接会让左表的一行出现在多行结果中，这是正常的；
- 把右表过滤条件错误地放进 `WHERE`，可能使 `LEFT JOIN` 实际效果变成 `INNER JOIN`；
- 连接列类型和字符集应尽量一致；
- 连接列通常需要合适的索引。

## 12. 子查询、CTE 和窗口函数

### 12.1 子查询

```sql
SELECT id, username
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
    WHERE amount >= 1000
);
```

也可以使用 `EXISTS`：

```sql
SELECT u.id, u.username
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM orders AS o
    WHERE o.user_id = u.id
      AND o.amount >= 1000
);
```

`EXISTS` 关心是否至少存在一行，不关心子查询具体返回什么值。

### 12.2 CTE

CTE 可以给临时结果集命名，提高复杂 SQL 的可读性：

```sql
WITH user_totals AS (
    SELECT user_id, SUM(amount) AS total_amount
    FROM orders
    GROUP BY user_id
)
SELECT u.username, t.total_amount
FROM user_totals AS t
JOIN users AS u ON u.id = t.user_id
WHERE t.total_amount >= 1000;
```

递归 CTE 可生成层级或序列：

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 10
)
SELECT n FROM numbers;
```

### 12.3 窗口函数

窗口函数在保留每一行的同时计算排名、累计值或分组统计：

```sql
SELECT
    user_id,
    amount,
    created_at,
    ROW_NUMBER() OVER (
        PARTITION BY user_id
        ORDER BY created_at DESC
    ) AS order_no
FROM orders;
```

- `OVER`：定义窗口；
- `PARTITION BY`：把结果分成窗口分区；
- `ROW_NUMBER`：为每个分区中的行编号；
- `RANK`：并列值排名相同，后续名次会跳号；
- `DENSE_RANK`：并列值排名相同，后续名次不跳号。

## 13. 约束与数据完整性

数据库约束用于防止不合法数据进入表中：

| 约束 | 含义 |
| --- | --- |
| `PRIMARY KEY` | 主键，唯一且非空 |
| `UNIQUE` | 唯一约束 |
| `NOT NULL` | 不允许空值 |
| `DEFAULT` | 默认值 |
| `CHECK` | 检查表达式，MySQL 8.0.16 起真正执行 |
| `FOREIGN KEY` | 外键，维护表间引用完整性 |

示例：

```sql
CREATE TABLE products (
    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_products_price CHECK (price >= 0),
    CONSTRAINT chk_products_stock CHECK (stock >= 0)
);
```

能由数据库稳定保证的核心规则，应尽量用约束表达，而不是只依赖应用代码。

## 14. 索引原理和使用

索引类似书的目录，用额外空间和写入成本换取查询速度。InnoDB 的普通索引和主键索引主要使用 B+ Tree 结构。

### 14.1 聚簇索引和二级索引

InnoDB 表的数据行按主键索引组织：

- 主键索引也叫聚簇索引，叶子节点保存完整行数据；
- 普通索引也叫二级索引，叶子节点通常保存索引列和主键值；
- 通过二级索引查询非索引列时，可能先得到主键，再回到聚簇索引取完整行，这称为回表。

因此，InnoDB 主键应尽量短小、稳定。随机且很长的主键可能增加索引空间和页分裂成本。

### 14.2 创建和删除索引

```sql
CREATE INDEX idx_users_username ON users (username);
CREATE UNIQUE INDEX uk_users_email ON users (email);
DROP INDEX idx_users_username ON users;
SHOW INDEX FROM users;
```

- `INDEX` 常缩写为 `idx`；
- `UNIQUE` 表示索引值必须唯一；
- 主键和唯一约束会自动建立相应索引。

### 14.3 联合索引和最左前缀

```sql
CREATE INDEX idx_users_status_created_at
ON users (status, created_at);
```

这个索引通常适合：

```sql
WHERE status = 1
WHERE status = 1 AND created_at >= '2026-01-01'
```

但只按 `created_at` 查询时，通常不能有效利用该索引的最左列定位。这被称为联合索引的最左前缀原则。

索引列顺序应根据实际查询中的等值条件、范围条件、排序、分组和选择性综合设计，不能只套用“选择性最高的列永远放最前面”之类的简单规则。

### 14.4 覆盖索引

如果查询需要的列全部包含在某个索引中，InnoDB 可能不必回表：

```sql
SELECT status, created_at, id
FROM users
WHERE status = 1
ORDER BY created_at DESC;
```

对于索引 `(status, created_at)`，二级索引叶子节点还包含主键 `id`，因此这条查询可能形成覆盖索引。

### 14.5 索引不一定越多越好

索引会带来：

- 占用磁盘和内存；
- `INSERT`、`UPDATE`、`DELETE` 时需要维护；
- 增加优化器选择成本；
- 冗余索引会浪费资源。

低选择性列、很小的表或频繁更新而很少查询的列，不一定值得单独建立索引。

## 15. EXPLAIN 分析执行计划

```sql
EXPLAIN
SELECT *
FROM users
WHERE email = 'alice@example.com';
```

MySQL 8.0 还支持：

```sql
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email = 'alice@example.com';
```

`EXPLAIN` 只展示估算的执行计划；`EXPLAIN ANALYZE` 会真正执行查询，并显示实际时间和行数。不要对可能修改数据的语句或高成本查询盲目使用分析功能。

传统 `EXPLAIN` 输出中常关注：

- `table`：当前访问的表；
- `type`：访问方式；
- `possible_keys`：可能使用的索引；
- `key`：实际选用的索引；
- `key_len`：使用的索引长度；
- `rows`：预计扫描行数；
- `filtered`：预计过滤后剩余百分比；
- `Extra`：额外信息。

`type` 常见值大致从更精确到扫描更多数据包括：

```text
const → eq_ref → ref → range → index → ALL
```

`ALL` 通常表示全表扫描，但全表扫描不必然错误。对于很小的表或需要返回大部分数据的查询，全表扫描可能更合理。

## 16. InnoDB 的关键原理

### 16.1 Buffer Pool

Buffer Pool 是 InnoDB 的主要内存缓存，用于保存经常访问的数据页和索引页。读取数据时优先在内存中寻找；修改数据时通常先修改内存页，再由后台线程写回磁盘。

这解释了为什么：

- MySQL 进程占用大量内存可能是正常的；
- 同一查询第二次执行可能更快；
- 不能只看磁盘文件就判断数据是否已安全提交。

### 16.2 Redo Log

Redo Log 即重做日志，记录数据页的物理修改信息，用于崩溃恢复。事务提交时，MySQL 可以先保证 redo 持久化，而不必立即把所有脏数据页写回其最终位置。

`redo` 的含义是“重做”：发生崩溃后，InnoDB 可重放已提交但尚未完整写入数据文件的修改。

### 16.3 Undo Log

Undo Log 即回滚日志，保存逻辑上的旧版本信息，主要用于：

- 事务回滚；
- MVCC 一致性读取。

`undo` 的含义是“撤销”。长时间不提交的事务可能阻碍旧版本清理，导致 Undo 空间增长。

### 16.4 Binlog

Binary Log，简称 Binlog，记录数据库变更事件，主要用于：

- 主从复制；
- 基于时间点恢复；
- 数据变更审计或订阅。

Binlog 属于 MySQL Server 层，Redo Log 属于 InnoDB 存储引擎层，两者用途不同，不能互相替代。

### 16.5 MVCC

`MVCC` = **Multi-Version Concurrency Control**，多版本并发控制。

InnoDB 利用事务信息和 Undo Log 构造数据的历史版本，使普通一致性读取在很多情况下不必阻塞正在修改数据的事务，从而提高并发能力。

MVCC 并不意味着所有操作都不加锁。更新、删除、锁定读和约束检查仍可能获取各种锁。

## 17. 事务与 ACID

事务是一组要么全部成功、要么全部失败的操作。例如转账必须同时扣减一个账户并增加另一个账户。

`ACID` 表示事务的四个重要性质：

- `A` = **Atomicity**，原子性：事务中的操作整体成功或整体回滚；
- `C` = **Consistency**，一致性：事务前后满足约束和业务规则；
- `I` = **Isolation**，隔离性：并发事务之间按隔离级别控制影响；
- `D` = **Durability**，持久性：事务提交后结果能够在故障后恢复。

### 17.1 事务基本命令

```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

COMMIT;
```

发生错误时：

```sql
ROLLBACK;
```

- `COMMIT`：提交并永久确认事务；
- `ROLLBACK`：回滚尚未提交的修改；
- `SAVEPOINT`：设置事务内的保存点。

```sql
START TRANSACTION;
UPDATE products SET stock = stock - 1 WHERE id = 10;
SAVEPOINT stock_updated;
INSERT INTO audit_logs(message) VALUES ('stock updated');
ROLLBACK TO SAVEPOINT stock_updated;
COMMIT;
```

### 17.2 autocommit

```sql
SELECT @@autocommit;
```

MySQL 默认开启自动提交。没有显式事务时，每条成功的 DML 语句通常作为独立事务自动提交。

关闭自动提交后，务必明确执行 `COMMIT` 或 `ROLLBACK`，避免长事务长期持锁和保留历史版本。

### 17.3 隔离级别

```sql
SELECT @@transaction_isolation;

SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

SQL 标准定义四种隔离级别：

| 隔离级别 | 含义 |
| --- | --- |
| `READ UNCOMMITTED` | 可读到其他事务未提交的数据 |
| `READ COMMITTED` | 每次读取只看已提交数据 |
| `REPEATABLE READ` | 同一事务的一致性读取通常保持同一视图 |
| `SERIALIZABLE` | 最强隔离，并发能力通常最低 |

InnoDB 默认一般是 `REPEATABLE READ`。隔离级别越高不等于所有业务场景越好，应结合一致性要求、并发量和应用逻辑选择。

## 18. 锁与死锁

InnoDB 常见锁概念包括：

- 共享锁（S Lock）：允许读取；
- 排他锁（X Lock）：用于修改；
- 记录锁（Record Lock）：锁住索引记录；
- 间隙锁（Gap Lock）：锁住索引记录之间的范围；
- Next-Key Lock：记录锁与间隙锁的组合；
- 意向锁（Intention Lock）：表级标记，表示事务准备在行上加锁；
- 元数据锁（MDL）：保护表结构与访问之间的一致性。

`MDL` = **Metadata Lock**，元数据锁。

锁定读取：

```sql
START TRANSACTION;

SELECT stock
FROM products
WHERE id = 10
FOR UPDATE;

UPDATE products
SET stock = stock - 1
WHERE id = 10 AND stock > 0;

COMMIT;
```

`FOR UPDATE` 会获取适合后续更新的锁。必须在事务中使用，并尽快提交。

### 18.1 死锁

两个事务各自持有对方需要的锁，并相互等待时可能形成死锁。InnoDB 会检测死锁并回滚其中一个事务。

查看最近一次死锁信息：

```sql
SHOW ENGINE INNODB STATUS\G
```

减少死锁的常用方法：

- 多个事务按一致顺序访问资源；
- 缩短事务，避免事务中进行慢网络调用；
- 为查询建立合适索引，减少锁定范围；
- 应用正确处理死锁错误，并在合适情况下重试整个事务；
- 不要只重试失败的单条 SQL，因为整个事务可能已回滚。

## 19. 用户、身份验证和权限

### 19.1 查看账户

```sql
SELECT user, host, plugin
FROM mysql.user;
```

查询 `mysql.user` 通常需要较高权限。

### 19.2 创建用户

```sql
CREATE USER 'app_user'@'localhost'
IDENTIFIED BY 'Use-A-Strong-Password';
```

允许指定网段连接：

```sql
CREATE USER 'app_user'@'10.%'
IDENTIFIED BY 'Use-A-Strong-Password';
```

`'app_user'@'%'` 表示可从任意来源主机尝试连接，范围很大，不应在没有网络访问控制的情况下随意使用。

### 19.3 授权和回收

```sql
GRANT SELECT, INSERT, UPDATE, DELETE
ON app_db.*
TO 'app_user'@'localhost';

SHOW GRANTS FOR 'app_user'@'localhost';

REVOKE DELETE
ON app_db.*
FROM 'app_user'@'localhost';
```

- `GRANT`：授予权限；
- `REVOKE`：回收权限；
- `app_db.*`：数据库中的所有对象；
- `*.*`：所有数据库的所有对象，权限范围很大。

MySQL 8.0 中应先用 `CREATE USER` 创建账户，再用 `GRANT` 授权，不要依赖旧版本中 `GRANT ... IDENTIFIED BY ...` 同时创建用户的写法。

### 19.4 修改密码和删除用户

```sql
ALTER USER 'app_user'@'localhost'
IDENTIFIED BY 'A-New-Strong-Password';

DROP USER 'app_user'@'localhost';
```

一般业务应用不应使用 root 账户。应为不同应用创建独立账户，并只授予实际需要的数据库和操作权限。

### 19.5 FLUSH PRIVILEGES 是否必需

使用 `CREATE USER`、`ALTER USER`、`GRANT`、`REVOKE` 等账户管理语句时，MySQL 会立即更新权限，一般不需要执行：

```sql
FLUSH PRIVILEGES;
```

只有直接修改授权表等特殊场景才可能需要重新加载。一般不应直接修改 `mysql.user`。

## 20. 配置文件和重要参数

Ubuntu 软件包安装时，常见配置位置包括：

```text
/etc/mysql/my.cnf
/etc/mysql/mysql.conf.d/mysqld.cnf
/etc/mysql/conf.d/
```

查看 MySQL 会读取哪些默认文件：

```bash
mysqld --verbose --help 2>/dev/null | grep -A 1 "Default options"
```

查看运行中的变量：

```sql
SHOW VARIABLES LIKE 'port';
SHOW VARIABLES LIKE 'datadir';
SHOW VARIABLES LIKE 'character_set_server';
SHOW VARIABLES LIKE 'collation_server';
SHOW VARIABLES LIKE 'max_connections';
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
```

常见参数：

- `port`：TCP 端口，默认 3306；
- `bind-address`：监听地址；
- `datadir`：数据文件目录；
- `max_connections`：最大连接数；
- `innodb_buffer_pool_size`：InnoDB 缓冲池大小；
- `character_set_server`：服务器默认字符集；
- `collation_server`：服务器默认排序规则；
- `slow_query_log`：是否启用慢查询日志；
- `long_query_time`：慢查询时间阈值。

修改配置前应先备份，并检查参数是否支持动态修改、是否需要重启。错误配置可能导致 MySQL 无法启动。

## 21. 连接、会话和运行状态

```sql
SHOW PROCESSLIST;
SHOW FULL PROCESSLIST;
SHOW STATUS LIKE 'Threads_connected';
SHOW STATUS LIKE 'Threads_running';
SHOW GLOBAL STATUS LIKE 'Connections';
```

- `SHOW PROCESSLIST`：查看当前连接和正在执行的语句；
- `Threads_connected`：当前打开的连接数；
- `Threads_running`：正在运行而非休眠的线程数；
- `Connections`：服务器启动以来尝试连接的累计次数。

终止某个会话：

```sql
KILL 123;
```

只终止当前语句而保留连接：

```sql
KILL QUERY 123;
```

执行前必须确认连接 ID 和影响。不要看到长时间运行的查询就直接终止，应先判断它是否是备份、结构变更或必要业务任务。

## 22. 慢查询和性能排查

性能问题应基于证据排查，而不是首先修改大量参数。

基本顺序：

1. 确认问题发生时间、具体接口和 SQL；
2. 查看系统 CPU、内存、磁盘 I/O 和连接数；
3. 查看慢查询日志或 Performance Schema；
4. 使用 `EXPLAIN` 和 `EXPLAIN ANALYZE` 检查执行计划；
5. 检查扫描行数、索引、排序、临时表和锁等待；
6. 修改 SQL 或索引后进行可重复测试；
7. 观察优化是否改善整体系统，而不只是单条查询。

### 22.1 慢查询日志

```sql
SHOW VARIABLES LIKE 'slow_query_log';
SHOW VARIABLES LIKE 'slow_query_log_file';
SHOW VARIABLES LIKE 'long_query_time';
```

临时启用示例：

```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;
```

动态设置可能在重启后失效。需要长期生效时应写入正确的配置文件，并评估日志空间和性能影响。

### 22.2 Performance Schema

`Performance Schema` 是 MySQL 内置的性能监控基础设施，可记录语句、等待、锁和内存等信息。它功能强大，但表较多。初学者可以先使用 `sys` 库中封装好的视图：

```sql
SELECT *
FROM sys.statement_analysis
ORDER BY total_latency DESC
LIMIT 10;
```

`sys` 库基于 Performance Schema 和 Information Schema 提供更容易阅读的诊断视图。

## 23. Information Schema、Performance Schema 和 sys

MySQL 8.0 包含几个重要系统数据库：

- `information_schema`：数据库、表、列、索引等元数据信息；
- `performance_schema`：运行时性能和等待事件；
- `sys`：对性能数据进行友好封装的视图；
- `mysql`：用户、权限、时区和系统组件等内部数据。

示例：

```sql
SELECT table_schema,
       table_name,
       table_rows,
       data_length,
       index_length
FROM information_schema.tables
WHERE table_schema = 'app_db'
ORDER BY data_length + index_length DESC;
```

- `I_S` 有时表示 `Information Schema`；
- `P_S` 有时表示 `Performance Schema`；
- `schema` 在这里表示数据库结构信息。

## 24. 备份与恢复

备份必须定期执行并实际验证恢复。只有备份文件存在，不能证明它一定可用。

### 24.1 mysqldump 逻辑备份

备份单个数据库：

```bash
mysqldump -u root -p \
  --single-transaction \
  --routines \
  --triggers \
  --events \
  app_db > app_db.sql
```

备份所有数据库：

```bash
mysqldump -u root -p --all-databases > all_databases.sql
```

常用选项：

- `--single-transaction`：对 InnoDB 使用一致性快照，减少锁表影响；
- `--routines`：包含存储过程和函数；
- `--triggers`：包含触发器；
- `--events`：包含事件调度器事件；
- `--no-data`：只导出结构；
- `--no-create-info`：只导出数据。

`mysqldump` 是逻辑备份工具，导出的是可重新执行的 SQL。对超大数据库，它可能较慢且恢复耗时较长。

### 24.2 恢复逻辑备份

```bash
mysql -u root -p -e "CREATE DATABASE app_db CHARACTER SET utf8mb4"
mysql -u root -p app_db < app_db.sql
```

恢复前应确认 SQL 文件内容、目标数据库和字符集。恢复操作可能覆盖或重复已有对象，不应直接在生产库上试验。

### 24.3 mysqlpump 与 MySQL Shell

MySQL 8.0 还可使用 MySQL Shell 的 Dump and Load 工具进行并行导出和导入。`mysqlpump` 虽曾提供并行逻辑备份，但在后续 MySQL 8.0 版本中已被弃用，新方案应优先评估 MySQL Shell。

### 24.4 物理备份和时间点恢复

大型生产数据库通常还会使用物理备份工具，并结合 Binlog 做时间点恢复：

- 全量备份提供某一时刻的基础数据；
- Binlog 记录之后的变更；
- 恢复时先还原全量备份，再重放到目标时间点。

`PITR` = **Point-in-Time Recovery**，基于时间点恢复。

物理备份、复制和高可用配置涉及更高的运维风险，应在隔离环境中验证完整流程。

## 25. 导入和导出文本数据

导出查询结果可以在系统终端使用批处理模式：

```bash
mysql -u app_user -p \
  --batch --raw \
  -e "SELECT id, username, email FROM app_db.users" \
  > users.tsv
```

- `TSV` = **Tab-Separated Values**，制表符分隔值；
- `CSV` = **Comma-Separated Values**，逗号分隔值；
- `--batch`：批处理输出；
- `--raw`：不转义输出内容。

`SELECT ... INTO OUTFILE` 由 MySQL 服务器进程在服务器文件系统上写文件，需要 `FILE` 权限，并受 `secure_file_priv` 限制：

```sql
SHOW VARIABLES LIKE 'secure_file_priv';
```

它与客户端重定向 `>` 的执行位置不同。

## 26. 常见错误与排查

### 26.1 Access denied for user

检查：

```sql
SELECT USER(), CURRENT_USER();
SHOW GRANTS;
```

- `USER()` 显示客户端提交的用户和来源；
- `CURRENT_USER()` 显示实际用于权限检查的 MySQL 账户。

常见原因包括密码错误、来源主机不匹配、账户不存在、身份验证插件不兼容或权限不足。

### 26.2 Can't connect to MySQL server

在 Ubuntu 中检查：

```bash
sudo systemctl status mysql
sudo ss -lntp | grep 3306
sudo journalctl -u mysql -n 100 --no-pager
```

还应检查主机名、端口、防火墙、`bind-address`、云安全组和网络路由。

### 26.3 Too many connections

```sql
SHOW VARIABLES LIKE 'max_connections';
SHOW STATUS LIKE 'Threads_connected';
SHOW FULL PROCESSLIST;
```

不要只提高 `max_connections`。应检查应用是否泄漏连接、连接池是否设置过大、查询是否过慢以及连接是否长时间空闲。

### 26.4 Lock wait timeout exceeded

表示事务等待锁超过阈值。应查找阻塞链和长事务，而不是反复盲目重试：

```sql
SELECT * FROM sys.innodb_lock_waits\G
```

处理前先确认阻塞事务正在做什么，避免误杀重要任务。

### 26.5 Data too long 或 Incorrect string value

- `Data too long`：值超过列定义长度；
- `Incorrect string value`：常与字符集不支持该字符有关；
- 检查表、列、连接的字符集与排序规则；
- 保存 emoji 应使用 `utf8mb4`，不要使用 MySQL 历史上的三字节 `utf8mb3`。

### 26.6 MySQL 无法启动

```bash
sudo systemctl status mysql
sudo journalctl -u mysql -b --no-pager
sudo mysqld --validate-config
```

常见原因有配置项拼写错误、端口冲突、数据目录权限错误、磁盘空间不足或不兼容的配置。不要在没有备份的情况下删除数据目录或 InnoDB 日志文件来“尝试修复”。

## 27. 安全开发建议

### 27.1 防止 SQL 注入

不要拼接用户输入：

```python
# 错误示例：用户输入可能改变 SQL 结构
sql = "SELECT * FROM users WHERE username = '" + username + "'"
```

应使用数据库驱动提供的参数化查询：

```python
cursor.execute(
    "SELECT id, username FROM users WHERE username = %s",
    (username,),
)
```

参数占位符形式由具体驱动决定。参数化查询保护的是数据值；表名、列名等标识符需要使用允许列表验证，不能直接作为普通值参数绑定。

### 27.2 最小权限

- 应用不用 root；
- 读服务只授予 `SELECT`；
- 迁移账户和运行时账户可以分离；
- 不把密码写入代码或提交到 Git；
- 数据库不应无必要地监听公网；
- 远程连接应配合防火墙、TLS、VPN 或私有网络。

### 27.3 数据变更习惯

执行高风险 SQL 前：

1. 确认当前服务器和数据库；
2. 用 `SELECT` 验证 `WHERE` 条件；
3. 估算影响行数；
4. 确认事务、锁和日志影响；
5. 准备备份或回滚方案；
6. 在测试环境先演练；
7. 生产执行后验证数据和系统指标。

## 28. 常用 SQL 和命令速查表

| 命令或缩写 | 英文全称或含义 | 用途 |
| --- | --- | --- |
| `DB` | Database | 数据库 |
| `DBMS` | Database Management System | 数据库管理系统 |
| `RDBMS` | Relational Database Management System | 关系型数据库管理系统 |
| `SQL` | Structured Query Language | 结构化查询语言 |
| `DDL` | Data Definition Language | 定义数据库对象 |
| `DML` | Data Manipulation Language | 修改数据 |
| `DQL` | Data Query Language | 查询数据 |
| `DCL` | Data Control Language | 权限控制 |
| `TCL` | Transaction Control Language | 事务控制 |
| `CRUD` | Create, Read, Update, Delete | 增删改查 |
| `CREATE` | 创建 | 创建数据库、表或用户 |
| `ALTER` | 修改 | 修改对象结构或用户 |
| `DROP` | 删除对象 | 删除库、表、索引或用户 |
| `TRUNCATE` | 截断 | 快速清空表 |
| `INSERT` | 插入 | 新增数据 |
| `SELECT` | 选择 | 查询数据 |
| `UPDATE` | 更新 | 修改数据 |
| `DELETE` | 删除 | 删除行 |
| `JOIN` | 连接 | 组合多张表 |
| `ASC` | ascending | 升序 |
| `DESC` | descending / describe | 降序，或描述表结构 |
| `AVG` | average | 平均值 |
| `MIN` | minimum | 最小值 |
| `MAX` | maximum | 最大值 |
| `PK` | Primary Key | 主键 |
| `UK` | Unique Key | 唯一键 |
| `FK` | Foreign Key | 外键 |
| `IDX` | Index | 索引 |
| `ACID` | Atomicity, Consistency, Isolation, Durability | 事务四大性质 |
| `MVCC` | Multi-Version Concurrency Control | 多版本并发控制 |
| `CTE` | Common Table Expression | 公共表表达式 |
| `JSON` | JavaScript Object Notation | JSON 数据格式 |
| `BLOB` | Binary Large Object | 二进制大对象 |
| `PITR` | Point-in-Time Recovery | 时间点恢复 |
| `mysqld` | MySQL daemon | MySQL 服务进程 |
| `mysql` | MySQL client | 命令行客户端 |
| `mysqldump` | MySQL dump | 逻辑备份工具 |
| `-u` | user | 连接用户名 |
| `-p` | password | 提示输入密码 |
| `-h` | host | 服务器地址 |
| `-P` | port | TCP 端口 |
| `\G` | vertical output | 纵向显示查询结果 |

## 29. 推荐学习顺序

初学者可以按以下顺序实践：

1. 安装 MySQL 8.0，理解 Server、客户端和端口；
2. 学会连接、退出、查看版本和获取帮助；
3. 使用 `CREATE DATABASE`、`CREATE TABLE` 建立简单结构；
4. 掌握 `INSERT`、`SELECT`、`UPDATE`、`DELETE`；
5. 学习 `WHERE`、`ORDER BY`、`GROUP BY` 和常用聚合函数；
6. 学习主键、唯一约束、外键和数据类型选择；
7. 通过实际的一对多模型练习 `JOIN`；
8. 理解索引、联合索引和 `EXPLAIN`；
9. 理解事务、ACID、隔离级别、锁和死锁；
10. 创建最小权限用户，练习备份和恢复；
11. 学习慢查询日志和基础性能排查；
12. 再进一步学习复制、高可用、分区和大规模数据治理。

学习 MySQL 的重点不是背诵全部语句，而是建立四个稳定的思维模型：数据如何建模、查询如何执行、并发如何保证一致性、出现故障后如何恢复。所有重要操作都应在测试数据上亲自练习，并养成先验证范围、再执行修改、最后检查结果的习惯。
