# EARS格式规范

## 概述
EARS (Easy Approach to Requirements Syntax) 是一种简化的需求语法格式，用于编写清晰、可测试的需求。

## EARS模式类型

### 1. Ubiquitous（普遍性）
**格式**: The \<system\> shall \<action\>
**用途**: 系统必须始终执行的行为
**示例**: The system shall display the current date on the main page

### 2. Event-driven（事件驱动）
**格式**: When \<trigger\> the \<system\> shall \<action\>
**用途**: 当特定事件发生时系统执行的行为
**示例**: When the user clicks the submit button the system shall validate all input fields

### 3. State-driven（状态驱动）
**格式**: While \<state\> the \<system\> shall \<action\>
**用途**: 当系统处于特定状态时执行的行为
**示例**: While the system is in maintenance mode the system shall display a warning message

### 4. Optional feature（可选特性）
**格式**: Where \<feature\> is included the \<system\> shall \<action\>
**用途**: 当包含特定特性时执行的行为
**示例**: Where email notification is included the system shall send a confirmation email

### 5. Unwanted behavior（不期望行为）
**格式**: The \<system\> shall not \<action\>
**用途**: 系统不应执行的行为
**示例**: The system shall not store passwords in plain text

## 编写规则

1. **使用主动语态**: 需求应使用主动语态而非被动语态
2. **单一行为**: 每个需求应只描述一个行为
3. **可验证性**: 需求必须能够被测试和验证
4. **无歧义性**: 使用清晰、明确的术语
5. **完整性**: 包含所有必要的前置条件和后置条件

## 验收标准格式

每个需求应包含验收标准，格式如下：
- Given: 初始条件/前置条件
- When: 触发动作
- Then: 期望结果/后置条件
