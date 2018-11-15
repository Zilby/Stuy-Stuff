class PPM
  attr_reader :width, :height, :max_color_value

  def initialize(pixels, options={})
    @pixels = pixels
    @width = pixels.first.size
    @height = pixels.size
    @max_color_value = options[:max_color_value] || 255
  end

  def stringify
    data = [header_string, image_string, '']
    data.join("\n")
  end

  def write(file)
    file.write(stringify)
  end

  private

  def header_string
    header_string = ["P3"]
    header_string << "#{@width} #{@height}"
    header_string << @max_color_value
    header_string.join("\n")
  end

  def image_string
    row_strings = @pixels.each { |row| convert_row_to_string(row) }
    row_strings.join("\n")
  end

  def convert_row_to_string(row_array)
    row_array.join(' ')
  end
end
