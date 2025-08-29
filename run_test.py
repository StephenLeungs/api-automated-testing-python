#!/usr/bin/env python3
"""
一键运行测试并生成 Allure 报告脚本
使用方法: python run_test.py
"""

import subprocess
import sys


def run_command(command, description):
    """运行命令并处理输出和错误"""
    print(f"\n{'=' * 50}")
    print(f"开始: {description}")
    print(f"执行命令: {command}")
    print(f"{'=' * 50}")

    try:
        # 执行命令，实时输出结果
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        print(f"\n✅ 完成: {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 错误: {description} 失败，退出码: {e.returncode}")
        return False
    except Exception as e:
        print(f"\n❌ 意外错误: {description} - {str(e)}")
        return False


def main():
    """主函数"""
    print("🚀 开始执行测试并生成Allure报告")

    # 第一步: 运行pytest测试
    pytest_success = run_command(
        "pytest",
        "运行pytest测试用例"
    )

    if not pytest_success:
        print("\n❌ 测试运行失败，停止生成报告")
        sys.exit(1)

    # 第二步: 生成Allure报告
    allure_success = run_command(
        "allure generate report/allure_report -o report/allure_html --clean",
        "生成Allure HTML报告"
    )

    if allure_success:
        print(f"\n🎉 所有步骤完成!")
        print(f"📊 测试报告已生成到: report/allure_html/index.html")
        print(f"💡 提示: 使用 'allure open report/allure_html' 命令在浏览器中打开报告")
    else:
        print(f"\n⚠️  测试运行成功，但报告生成失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
