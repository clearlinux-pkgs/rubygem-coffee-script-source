#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-coffee-script-source
Version  : 1.10.0
Release  : 7
URL      : https://rubygems.org/downloads/coffee-script-source-1.10.0.gem
Source0  : https://rubygems.org/downloads/coffee-script-source-1.10.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
No detailed description available

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n coffee-script-source-1.10.0
gem spec %{SOURCE0} -l --ruby > rubygem-coffee-script-source.gemspec

%build
gem build rubygem-coffee-script-source.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
coffee-script-source-1.10.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/coffee-script-source-1.10.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/coffee-script-source-1.10.0/lib/coffee_script/coffee-script.js
/usr/lib64/ruby/gems/2.3.0/gems/coffee-script-source-1.10.0/lib/coffee_script/source.rb
/usr/lib64/ruby/gems/2.3.0/specifications/coffee-script-source-1.10.0.gemspec
