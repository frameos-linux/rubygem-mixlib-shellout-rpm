# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{mixlib-shellout}
  s.version = "1.1.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Opscode"]
  s.date = %q{2012-08-06}
  s.description = %q{Run external commands on Unix or Windows}
  s.email = %q{info@opscode.com}
  s.extra_rdoc_files = ["README.md", "LICENSE"]
  s.files = ["LICENSE", "README.md", "lib/mixlib/shellout.rb", "lib/mixlib/shellout/windows/core_ext.rb", "lib/mixlib/shellout/exceptions.rb", "lib/mixlib/shellout/version.rb", "lib/mixlib/shellout/unix.rb", "lib/mixlib/shellout/windows.rb"]
  s.homepage = %q{http://wiki.opscode.com/}
  s.require_paths = ["lib"]
  s.rubygems_version = %q{1.3.7}
  s.summary = %q{Run external commands on Unix or Windows}

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<rspec>, [">= 0"])
    else
      s.add_dependency(%q<rspec>, [">= 0"])
    end
  else
    s.add_dependency(%q<rspec>, [">= 0"])
  end
end
