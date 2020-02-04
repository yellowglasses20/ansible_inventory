from setuptools import setup, find_packages

__author__ = 'makoto yano'


setup(
    name='dynamic_ansible_inventory',  # ライブラリの名前
    version='0.2',  # バージョン
    description='create inventory file for ansible',  # 解説
    author='makoto yano',  # 作った人
    author_email='yano.makoto20@gmail.com',  # 作った人の連絡先
    url='https://github.com/yellowglasses20/ansible_inventory',  # URL(Githubリポジトリ)
    classifiers=[  # 注記事項(開発ステータス,利用目的,LICENSEなど)
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['dynamic_ansible_inventory'],  # 梱包するコードの場所. setuptoolsのfind_packages()でパッケージなdirectoryを捜索&よしなに突っ込んでくれます
    include_package_data=True,  # ソースコード(*.py)以外のファイルも入れるか否か
    keywords=['ansible', 'inventory'],  # キーワード
    license='Apache Software License',  # ライセンス
)