require 'spec_helper'
describe 'nginxboss' do

  context 'with defaults for all parameters' do
    it { should contain_class('nginxboss') }
  end
end
